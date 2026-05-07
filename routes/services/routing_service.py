import requests
from django.conf import settings

def get_route(start_coords, end_coords):

    url = "https://api.openrouteservice.org/v2/directions/driving-car"

    headers = {
        "Authorization": settings.ORS_API_KEY,
        "Content-Type": "application/json"
    }

    body = {
        "coordinates": [
            start_coords,
            end_coords
        ]
    }

    response = requests.post(url, json=body, headers=headers)

    return response.json()