from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from waitress import serve
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///iris.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Iris(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sepal_length = db.Column(db.Float)
    sepal_width = db.Column(db.Float)
    petal_length = db.Column(db.Float)
    petal_width = db.Column(db.Float)
    prediction = db.Column(db.String(100))

@app.route('/add_records', methods=['POST'])
def add_rec():
    data = request.get_json()
    new_rec = Iris(sepal_length=data['sl'], sepal_width=data['sw'], petal_length=data['pl'], petal_width=data['pw'], prediction=data['pred'])
    db.session.add(new_rec)
    db.session.commit()
    return 'Record added successfully', 200

@app.route('/show_records', methods=['GET'])
def show_rec():
    records = Iris.query.all()
    return jsonify([{'id': rec.id, 'sepal_length': rec.sepal_length, 'sepal_width': rec.sepal_width, 'petal_length': rec.petal_length, 'petal_width': rec.petal_width, 'prediction': rec.prediction} for rec in records])
if __name__=='__main__':
    with app.app_context():
        db.create_all()
    serve(app, host='0.0.0.0',port=8001)