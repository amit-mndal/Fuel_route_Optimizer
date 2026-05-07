from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="fuel_optimizer")

def get_coordinates(place):
    location = geolocator.geocode(place)

    return [location.longitude, location.latitude]