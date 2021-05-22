from flask import Flask, jsonify, request 
from webscraper import scrape_therapists

app = Flask(__name__)

@app.route("/locations/<address>", methods=['GET'])
def get_location(address):
    return jsonify({'result': address})

if __name__ == '__main__':
    app.run(debug=True)