import json
from math import sin, cos, sqrt, atan2, radians


def load_data(json_filepath):
    with open(json_filepath, 'r', encoding='utf-8') as json_file:
        return json.loads(json_file.read())


def get_biggest_bar(bars):
    biggest_bar = max(bars, key=lambda bar: bar_size(bar))
    return biggest_bar


def get_smallest_bar(bars):
    smallest_bar = min(bars, key=lambda bar: bar_size(bar))
    return smallest_bar


def get_closest_bar(bars, user_longitude, user_latitude):
    closest_bar = min(bars, key=lambda bar:
                      get_distance_between_bars(
                          user_longitude,
                          user_latitude,
                          get_bar_longitude(bar),
                          get_bar_latitude(bar)
                      ))
    return closest_bar


def get_bar_longitude(bar):
    return float(bar['geometry']['coordinates'][0])


def get_bar_latitude(bar):
    return float(bar['geometry']['coordinates'][1])


def bar_size(bar):
    return bar['properties']['Attributes']['SeatsCount']


def get_bar_name(bar):
    return bar['properties']['Attributes']['Name']


def get_distance_between_bars(lon1, lat1, lon2, lat2):
    """
    How to calculate distance between Latitude/Longitude points:
    https://www.movable-type.co.uk/scripts/latlong.html
    :param lon1: user's longitude
    :param lat1: user's latitude
    :param lon2: bar's longitude
    :param lat2: bar's latitude
    :return: distance between two points
    """
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    R = 6373.0
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    return distance

if __name__ == '__main__':
    json_filepath = input('Input a path to json-file:')
    loaded_data = load_data(json_filepath)
    user_longitude, user_latitude = \
        input('Input your longitude and latitude:').split(' ')
    bars = loaded_data['features']
    biggest_bar = get_biggest_bar(bars)
    smallest_bar = get_smallest_bar(bars)
    closest_bar = get_closest_bar(
        bars, float(user_longitude), float(user_latitude))
    print("The biggest bar:", get_bar_name(biggest_bar))
    print("The smallest bar:", get_bar_name(smallest_bar))
    print("The closest bar:", get_bar_name(closest_bar))
