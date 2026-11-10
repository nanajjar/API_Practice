"""Functions for retrieving city information from Open-Meteo Geocoding."""

from api_client import get_json

GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"


def find_city(city_name):
    """Return the first matching city dictionary, or None if not found."""
    params = {
        # TODO: Set "name" to city_name.
        # TODO: Set "count" to 1.
    }

    # TODO: Call get_json(GEOCODING_URL, params).
    # TODO: Find the list under the "results" key.
    #       Hint: data.get("results", []) is useful if the key is missing.
    # TODO: Return the first result, or None if there are no results.
    raise NotImplementedError("Complete find_city() in cities.py")


def get_coordinates(city_name):
    """Return (latitude, longitude), or None if the city is not found."""
    # TODO: Call find_city(city_name).
    # TODO: Return None if there is no match.
    # TODO: Return a tuple containing latitude and longitude.
    raise NotImplementedError("Complete get_coordinates() in cities.py")


def get_city_info(city_name):
    """Return a simplified dictionary of city details, or None.

    Include these keys: name, country, latitude, longitude, timezone.
    """
    # TODO: Call find_city(city_name).
    # TODO: Return None if there is no match.
    # TODO: Return a new dictionary with the five fields listed above.
    raise NotImplementedError("Complete get_city_info() in cities.py")
