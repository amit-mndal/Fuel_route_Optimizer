import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

import pandas as pd
from geopy.geocoders import Nominatim
from time import sleep

from routes.services.fuel_service import filter_stations_by_states

# Route states
states = ["NY", "NJ", "PA", "OH", "IN", "IL"]

# Filter stations
df = filter_stations_by_states(states)

# Geocoder
geolocator = Nominatim(user_agent="fuel_optimizer")

latitudes = []
longitudes = []

for index, row in df.iterrows():

    address = f"{row['Address']}, {row['City']}, {row['State']}, USA"

    try:

        location = geolocator.geocode(address)

        if location:

            latitudes.append(location.latitude)
            longitudes.append(location.longitude)

            print(f"SUCCESS: {address}")

        else:

            latitudes.append(None)
            longitudes.append(None)

            print(f"FAILED: {address}")

    except Exception as e:

        latitudes.append(None)
        longitudes.append(None)

        print(f"ERROR: {address}")

    sleep(1)

# Add coordinates
df["latitude"] = latitudes
df["longitude"] = longitudes

# Save processed stations
df.to_csv("data/filtered_stations.csv", index=False)

print("DONE")