
from flask import Flask, jsonify
from predictor import get_prediction
from scraper import get_latest_result

app = Flask(__name__)

@app.route('/api/result', methods=['GET'])
def result():
    return jsonify(get_latest_result())

@app.route('/api/predict', methods=['GET'])
def predict():
    return jsonify(get_prediction())

if __name__ == '__main__':
    app.run()
