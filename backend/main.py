import requests
import secret_token
from flask import Flask, jsonify, request 
from webscraper import scrape_therapists

app = Flask(__name__)

@app.route("/locations/<lat>/<lng>", methods=['GET'])
def get_location(lat, lng):
    url = 'https://maps.googleapis.com/maps/api/geocode/json?latlng={},{}&key={}'.format(lat, lng, secret_token.MAPS_API_KEY)
    r = requests.get(url)
    results = r.json()['results']
    postal_code = results[0]['address_components'][-1]['short_name']
    link = "https://www.psychologytoday.com/us/therapists?search=" + postal_code
    return link

if __name__ == '__main__':
    app.run(debug=True)