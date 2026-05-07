from geopy.distance import geodesic

MAX_RANGE = 500
SAFE_RANGE = 400
MPG = 10


def optimize_fuel_stops(route_coords, stations):

    fuel_stops = []

    total_cost = 0

    used_stations = set()

    current_point = route_coords[0]

    distance_since_last_stop = 0

    sampled_route = route_coords[::500]

    for next_point in sampled_route:

        segment_distance = geodesic(
            current_point,
            next_point
        ).miles

        distance_since_last_stop += segment_distance

        # Refuel only near safe range
        if distance_since_last_stop < SAFE_RANGE:

            current_point = next_point
            continue

        reachable_stations = []

        for station in stations:

            station_name = station["truckstop_name"]

            if station_name in used_stations:
                continue

            station_point = (
                station["latitude"],
                station["longitude"]
            )

            distance_to_station = geodesic(
                next_point,
                station_point
            ).miles

            if distance_to_station <= 50:

                reachable_stations.append(station)

        if not reachable_stations:
            continue

        # Cheapest station nearby
        cheapest_station = min(
            reachable_stations,
            key=lambda x: x["price"]
        )

        used_stations.add(
            cheapest_station["truckstop_name"]
        )

        gallons_needed = SAFE_RANGE / MPG

        fuel_cost = gallons_needed * cheapest_station["price"]

        total_cost += fuel_cost

        fuel_stops.append({

            "truckstop_name":
                cheapest_station["truckstop_name"],

            "city":
                cheapest_station["city"].strip(),

            "state":
                cheapest_station["state"],

            "price_per_gallon":
                round(cheapest_station["price"], 2),

            "gallons_purchased":
                round(gallons_needed, 2),

            "estimated_fuel_cost":
                round(fuel_cost, 2)
        })

        distance_since_last_stop = 0

        current_point = next_point

    return fuel_stops, round(total_cost, 2)