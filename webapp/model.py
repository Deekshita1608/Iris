from sklearn import datasets
import pickle
from sklearn.naive_bayes import GaussianNB

# Load the iris dataset
iris = datasets.load_iris()
X_train = iris.data
y_train = iris.target

# Create and train the model
model = GaussianNB()
model.fit(X_train, y_train)

# Save the trained model
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)
    
print("Model trained and saved successfully as 'model.pkl'")