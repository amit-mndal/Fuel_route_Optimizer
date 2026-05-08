import pandas as pd
from geopy.distance import geodesic

fuel_df = pd.read_csv("data/filtered_stations.csv")


def find_nearby_stations(route_coords, max_distance=100):

    nearby_stations = []

    # SAMPLE FEWER POINTS FOR SPEED
    sampled_route = route_coords[::100]

    for _, row in fuel_df.iterrows():

        try:
            lat = float(row["latitude"])
            lon = float(row["longitude"])
            
            if pd.isna(lat) or pd.isna(lon):
                continue
            
            station_point = (lat, lon)
            
        except:
            continue

        for route_point in sampled_route:

            distance = geodesic(
                route_point,
                station_point
            ).miles

            if distance <= max_distance:

                nearby_stations.append({

                    "truckstop_name":
                        row["Truckstop Name"],

                    "city":
                        row["City"],

                    "state":
                        row["State"],

                    "price":
                        float(row["Retail Price"]),

                    "latitude":
                        float(row["latitude"]),

                    "longitude":
                        float(row["longitude"])
                })

                break

    print("Nearby Stations Found:", len(nearby_stations))

    return nearby_stations