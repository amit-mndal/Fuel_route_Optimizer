import pandas as pd
from geopy.geocoders import Nominatim
from time import sleep

# Load CSV
df = pd.read_csv("data/fuel-prices-for-be-assessment.csv")

# Geocoder
geolocator = Nominatim(user_agent="fuel_optimizer")

# New columns
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

# Add columns
df["latitude"] = latitudes
df["longitude"] = longitudes

# Save processed CSV
df.to_csv("data/processed_fuel_prices.csv", index=False)

print("DONE")