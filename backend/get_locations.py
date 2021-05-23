import requests
import secret_token

# getting all therapists
def get_therapist(lat, lng):
    link = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=' + str(lat) +"," + str(lng) + "&radius=5000&type=doctor&keyword=therapist&key=" + secret_token.MAPS_API_KEY
    places = []
    r = requests.get(link)
    results = r.json()['results']
    id = 1
    for i in results:
        name = i['name']
        address = i['vicinity']
        coords = [i['geometry']['location']['lat'], i['geometry']['location']['lng']]
        rating = i['rating']
        numRatings = i['user_ratings_total']
        
        entry = {
            'name': name,
            'address': address,
            'coords': coords,
            'rating': rating,
            'numRatings': numRatings,
            'id': id
        }
        places.append(entry)
        id += 1
    return places

# getting all psychiatrists 
def get_psychiatrist(lat, lng):
    link = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=' + str(lat) +"," + str(lng) + "&radius=5000&type=doctor&keyword=psychiatrist&key=" + secret_token.MAPS_API_KEY
    places = []
    r = requests.get(link)
    results = r.json()['results']
    for i in results:
        name = i['name']
        address = i['vicinity']
        coords = [i['geometry']['location']['lat'], i['geometry']['location']['lng']]
        rating = i['rating']
        numRatings = i['user_ratings_total']
        
        entry = {
            'name': name,
            'address': address,
            'coords': coords,
            'rating': rating,
            'numRatings': numRatings
        }
        places.append(entry)
    return places
