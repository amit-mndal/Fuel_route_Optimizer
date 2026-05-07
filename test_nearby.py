import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

import polyline

from routes.services.utils import get_coordinates
from routes.services.routing_service import get_route
from routes.services.fuel_service import find_nearby_stations

# Start/end
start = get_coordinates("New York")
end = get_coordinates("Chicago")

# Get route
route = get_route(start, end)

# Decode route
encoded_geometry = route["routes"][0]["geometry"]

route_coords = polyline.decode(encoded_geometry)

print("Route points:", len(route_coords))

# Find stations
stations = find_nearby_stations(route_coords)

print("Nearby Stations Found:", len(stations))

print("\nFirst 5 Stations:\n")

for station in stations[:5]:
    print(station)