"""Shared helper for communicating with HTTP APIs."""

import requests


def get_json(url, params):
    """Send a GET request and return the decoded JSON data.
    Args:
        url (str): API endpoint.
        params (dict): Query parameters.
    Returns:
        dict: The JSON response decoded into Python data.
    Raises:
        requests.RequestException: If the request fails.
    """
    # TODO 1: Use requests.get(url, params=params, timeout=10).
    # TODO 2: Raise an exception for unsuccessful HTTP responses.
    # TODO 3: Convert the response to Python data with .json().
    # TODO 4: Return the decoded data.
    
    raise NotImplementedError("Complete get_json() in api_client.py")
