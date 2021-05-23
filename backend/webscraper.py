import requests
import secret_token

from therapist_model import Therapist

def get_therapist(lat, lng):
    link = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=' + lat +"," + lng + "&radius=10000&type=doctor&keyword=therapist&key=" + secret_token.MAPS_API_KEY
    r = requests.get(link)
    results = r.json()['results']
    return results

print(get_therapist(40.7297, -73.8163))