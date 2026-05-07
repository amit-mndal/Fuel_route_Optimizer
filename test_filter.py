import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from routes.services.fuel_service import filter_stations_by_states

states = ["NY", "NJ", "PA", "OH", "IN", "IL"]

filtered = filter_stations_by_states(states)

print(filtered.head())

print("Total Stations:", len(filtered))