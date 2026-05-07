# import pandas as pd
# from geopy.distance import geodesic

# # Load processed stations
# fuel_df = pd.read_csv("data/filtered_stations.csv")


# def find_nearby_stations(route_coords, max_distance=20):

#     nearby_stations = []

#     for _, row in fuel_df.iterrows():

#         # Skip missing coordinates
#         if pd.isna(row["latitude"]) or pd.isna(row["longitude"]):
#             continue

#         station_point = (row["latitude"], row["longitude"])

#         # Check distance from route
#         for route_point in route_coords:

#             distance = geodesic(route_point, station_point).miles

#             if distance <= max_distance:

#                 nearby_stations.append({
#                     "truckstop_name": row["Truckstop Name"],
#                     "city": row["City"],
#                     "state": row["State"],
#                     "price": row["Retail Price"],
#                     "latitude": row["latitude"],
#                     "longitude": row["longitude"]
#                 })

#                 break

#     return nearby_stations










import pandas as pd
from geopy.distance import geodesic

# Load processed stations
fuel_df = pd.read_csv("data/filtered_stations.csv")


def find_nearby_stations(route_coords, max_distance=20):

    nearby_stations = []

    # SAMPLE ROUTE POINTS
    sampled_route = route_coords[::200]

    for _, row in fuel_df.iterrows():

        # Skip missing coords
        if pd.isna(row["latitude"]) or pd.isna(row["longitude"]):
            continue

        station_point = (
            row["latitude"],
            row["longitude"]
        )

        # Compare with sampled route only
        for route_point in sampled_route:

            distance = geodesic(
                route_point,
                station_point
            ).miles

            if distance <= max_distance:

                nearby_stations.append({
                    "truckstop_name": row["Truckstop Name"],
                    "city": row["City"],
                    "state": row["State"],
                    "price": row["Retail Price"],
                    "latitude": row["latitude"],
                    "longitude": row["longitude"]
                })

                break

    return nearby_stations