from TheraTracker.backend.webscraper import scrape_therapists
from flask import Flask, jsonify, request 
from webscraper import scrape_therapists

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    return str(scrape_therapists('https://www.psychologytoday.com/us/therapists?search=11366'))

if __name__ == '__main__':
    app.run(debug=True)