# Weather API Practice - Starter Repository

In this activity you'll use two public [Open-Meteo](https://open-meteo.com/) endpoints to explore cities and current weather. You'll build the solution **one function at a time**, keeping API communication separate from display and user interaction.

## Getting started

1. Install Python 3.10 or later.
2. From this repository's directory, install the one external library:

   python -m pip install -r requirements.txt

3. Run the starter program:

   python main.py

4. Complete the `TODO` markers in the suggested order below. The starter program intentionally raises `NotImplementedError` for tasks you haven't implemented yet.

## Project layout

weather_api/
├── main.py                 # Menu and user interaction
├── api_client.py           # Reusable HTTP GET + JSON helper
├── cities.py               # Geocoding and city information
├── weather.py              # Current weather information
├── requirements.txt
├── .gitignore
├── README.md

## Useful API endpoints

- Geocoding: `https://geocoding-api.open-meteo.com/v1/search`
- Current weather: `https://api.open-meteo.com/v1/forecast`

Try this in a browser before writing code:

`https://geocoding-api.open-meteo.com/v1/search?name=Charlotte&count=1`

Notice that `results` is a **list of dictionaries**. If no matching city is found, the `results` key may be missing.

## Part 1 - Make an API request

Complete `get_json()` in `api_client.py`:

- Send a GET request to `url` with the given `params`.
- Use a timeout, check for HTTP errors, and convert the response using `.json()`.
- Return the resulting Python data.

This function should **not** print anything or ask for user input.

## Part 2 - Reusable city functions

Complete the functions in `cities.py`:

1. `find_city(city_name)`: Ask the Geocoding API for one result. Return the first city dictionary or `None` if there is no match.
2. `get_coordinates(city_name)`: Return `(latitude, longitude)` or `None` if no city is found.
3. `get_city_info(city_name)`: Return a dictionary containing the name, country, latitude, longitude, and timezone, or `None`.

Use `find_city()` from the other two functions rather than repeating the API request code.

## Challenge 1 - City Explorer

Complete `city_explorer()` in `main.py`:

- Prompt for a city.
- Call `get_city_info()`.
- Display name, country, latitude, longitude, and timezone.
- Show a friendly message if the city is not found.

## Challenge 2 - Compare Two Cities

Complete `compare_cities()` in `main.py`:

- Prompt for two city names.
- Call `get_coordinates()` for each city.
- Compare their **latitudes** (larger latitude means farther north).
- Handle a missing city and equal latitudes.

## Challenge 3 - Weather Explorer

Complete `get_weather(latitude, longitude)` in `weather.py`:

- Request `current=temperature_2m,wind_speed_10m` from the Forecast API.
- Extract both values from the nested `current` dictionary.
- Return `(temperature, wind_speed)`.

Then complete `weather_explorer()` in `main.py`:

- Prompt for a city and look up its coordinates.
- Call `get_weather()` and display temperature in **°C** and wind speed in **km/h** (the API defaults for these variables).
- Handle missing cities.

**Optional:** Keep asking for cities until the user types `quit`.

## Design reminders

- Put **network requests** in `api_client.py`.
- Put **data retrieval and extraction** in `cities.py` and `weather.py`.
- Put **prompts and output** in `main.py`.
- Return values from functions; do not print inside the API or data-processing functions.
- API calls can fail. Once the basic exercise works, consider catching `requests.RequestException` in the command-line interface and showing an understandable error.
