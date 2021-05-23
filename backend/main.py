import requests
import secret_token
from flask import Flask, jsonify
from flask_cors import CORS
from webscraper import get_therapist, get_psychiatrist

app = Flask(__name__)

@app.route("/therapist/<lat>/<lng>", methods=['GET'])
def therapist(lat, lng):
    return jsonify(get_therapist(lat, lng))

@app.route("/psychiatrist/<lat>/<lng>", methods=['GET'])
def psychiatrist(lat, lng):
    final_result = []
    return jsonify(get_psychiatrist(lat, lng))

if __name__ == '__main__':
    app.run(debug=True)