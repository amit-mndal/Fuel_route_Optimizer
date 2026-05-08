from geopy.distance import geodesic

SAFE_RANGE = 500
MPG = 10


def optimize_fuel_stops(route_coords, stations):

    fuel_stops = []

    total_cost = 0

    used_stations = set()

    total_distance = 0

    previous_point = route_coords[0]

    sampled_route = route_coords[::10]

    for point in sampled_route:

        segment_distance = geodesic(
            previous_point,
            point
        ).miles

        total_distance += segment_distance

        previous_point = point

        # Need refuel every SAFE_RANGE miles
        if total_distance < SAFE_RANGE:
            continue

        nearby = []

        for station in stations:

            station_id = (
                station["truckstop_name"],
                station["city"]
            )

            if station_id in used_stations:
                continue

            station_point = (
                station["latitude"],
                station["longitude"]
            )

            dist = geodesic(
                point,
                station_point
            ).miles

            if dist <= 150:

                nearby.append(station)

        if not nearby:
            continue

        cheapest = min(
            nearby,
            key=lambda x: x["price"]
        )

        gallons = SAFE_RANGE / MPG

        fuel_cost = gallons * cheapest["price"]

        fuel_stops.append({

            "truckstop_name":
                cheapest["truckstop_name"],

            "city":
                cheapest["city"],

            "state":
                cheapest["state"],

            "price_per_gallon":
                round(cheapest["price"], 2),

            "gallons_purchased":
                round(gallons, 2),

            "estimated_fuel_cost":
                round(fuel_cost, 2)
        })

        total_cost += fuel_cost

        used_stations.add((
            cheapest["truckstop_name"],
            cheapest["city"]
        ))

        # RESET AFTER REFUEL
        total_distance = 0

    return fuel_stops, round(total_cost, 2)