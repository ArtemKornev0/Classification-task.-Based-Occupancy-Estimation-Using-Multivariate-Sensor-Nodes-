from flask import Flask, request, jsonify
import pickle
import numpy as np
from sklearn.ensemble import RandomForestClassifier


with open('./model.pkl', 'rb') as pkl_file:
    model = pickle.load(pkl_file)

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    features = request.json
    features = [float(elem) for elem in features.split(',')]
    features = np.array(features)
    features = features.reshape(1, 16)
    prediction = model.predict(features)
    return  jsonify(float(prediction[0]))

if __name__ == '__main__':

    app.run('localhost', 5000)
