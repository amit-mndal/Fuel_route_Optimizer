from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import polyline

from .serializers import RouteSerializer

from .services.utils import get_coordinates
from .services.routing_service import get_route
from .services.fuel_service import find_nearby_stations
from .services.optimizer import optimize_fuel_stops


class RouteOptimizationAPIView(APIView):

    def post(self, request):

        serializer = RouteSerializer(data=request.data)

        if not serializer.is_valid():

            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

        start_location = serializer.validated_data["start"]
        finish_location = serializer.validated_data["finish"]

        # Geocode
        start_coords = get_coordinates(start_location)
        finish_coords = get_coordinates(finish_location)

        # Route API
        route = get_route(start_coords, finish_coords)

        route_data = route["routes"][0]

        # Distance
        distance_meters = route_data["summary"]["distance"]

        distance_miles = round(
            distance_meters * 0.000621371,
            2
        )

        # Decode route
        encoded_geometry = route_data["geometry"]

        route_coords = polyline.decode(encoded_geometry)

        # Nearby stations
        nearby_stations = find_nearby_stations(route_coords)

        # Optimize fuel
        fuel_stops, total_cost = optimize_fuel_stops(
            route_coords,
            nearby_stations
        )

        return Response({

        "start": start_location,

        "finish": finish_location,

        "distance_miles": distance_miles,

        "total_fuel_cost": total_cost,

        "fuel_stops": fuel_stops,

        "nearby_station_count": len(nearby_stations),

        "route_points": len(route_coords),

        "route_geometry": encoded_geometry
        })