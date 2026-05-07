import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from routes.services.utils import get_coordinates
from routes.services.routing_service import get_route

start = get_coordinates("New York")
end = get_coordinates("Chicago")

print("START:", start)
print("END:", end)

route = get_route(start, end)

# ADD THIS PART HERE
segments = route["routes"][0]["segments"][0]["steps"]

states_found = set()

for step in segments:
    print(step["instruction"])

# EXISTING CODE CONTINUES
import polyline

route_data = route["routes"][0]

distance_meters = route_data["summary"]["distance"]

distance_miles = distance_meters * 0.000621371

print("Distance in miles:", round(distance_miles, 2))

encoded_geometry = route_data["geometry"]

decoded_coords = polyline.decode(encoded_geometry)

print("Total Route Points:", len(decoded_coords))

print("First 5 Coordinates:")
print(decoded_coords[:5])