from flask import Flask, render_template, request
import pickle
import requests
from waitress import serve

DB_POST_URI='http://dbapp:8001/add_records'
DB_GET_URI='http://dbapp:8001/show_records'

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        sepal_length = float(request.form['sepal_length'])
        sepal_width = float(request.form['sepal_width'])
        petal_length = float(request.form['petal_length'])
        petal_width = float(request.form['petal_width'])
        prediction = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])
        pred=''
        if prediction[0]==0:
            pred='Iris Setosa'
        elif prediction[0]==1:
            pred='Iris Versicolor'
        elif prediction[0]==2:
            pred='Iris Virginica'
        requests.post(url=DB_POST_URI, json={'sl':sepal_length, 'sw':sepal_width, 'pl':petal_length, 'pw':petal_width, 'pred':pred})
        return render_template('index.html', prediction=pred)
    return render_template('index.html')

@app.route('/show', methods=['GET'])
def history():
    records=requests.get(url=DB_GET_URI)
    return render_template('history.html', entries=records.json())
if __name__=='__main__':
    serve(app, host='0.0.0.0',port=8000)