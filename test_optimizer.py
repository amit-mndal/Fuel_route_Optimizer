import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

import polyline

from routes.services.utils import get_coordinates
from routes.services.routing_service import get_route
from routes.services.fuel_service import find_nearby_stations
from routes.services.optimizer import optimize_fuel_stops

# Start/end
start = get_coordinates("New York")
end = get_coordinates("Chicago")

# Route
route = get_route(start, end)

encoded_geometry = route["routes"][0]["geometry"]

route_coords = polyline.decode(encoded_geometry)

# Nearby stations
stations = find_nearby_stations(route_coords)

print("Nearby stations:", len(stations))

# Optimize
fuel_stops, total_cost = optimize_fuel_stops(
    route_coords,
    stations
)

print("\nFuel Stops:\n")

for stop in fuel_stops:
    print(stop)

print("\nTotal Fuel Cost:", total_cost)