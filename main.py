"""Command-line interface for the three weather API lab challenges."""

from cities import get_city_info, get_coordinates
from weather import get_weather


def city_explorer():
    """Challenge 1: Display information about a city."""
    # TODO: Ask the user to enter a city name.
    # TODO: Call get_city_info().
    # TODO: If the result is None, print a friendly message.
    # TODO: Otherwise print name, country, latitude, longitude, and timezone.
    raise NotImplementedError("Complete city_explorer() in main.py")


def compare_cities():
    """Challenge 2: Identify which of two cities is farther north."""
    # TODO: Prompt for two city names.
    # TODO: Call get_coordinates() for both cities.
    # TODO: Check for missing results before using the tuples.
    # TODO: Compare latitude (the first value of each tuple).
    # TODO: Print which city is farther north, or if latitudes match.
    raise NotImplementedError("Complete compare_cities() in main.py")


def weather_explorer():
    """Challenge 3: Display current temperature and wind speed for a city."""
    # TODO: Prompt for a city name.
    # TODO: Call get_coordinates() and handle missing results.
    # TODO: Pass coordinates to get_weather().
    # TODO: Display temperature in °C and wind speed in km/h.
    raise NotImplementedError("Complete weather_explorer() in main.py")


def main():
    """Show the menu and run the selected challenge."""
    while True:
        print("\nWeather API Lab")
        print("1. City Explorer")
        print("2. Compare Two Cities")
        print("3. Weather Explorer")
        print("Q. Quit")

        choice = input("Choose an option: ").strip().lower()

        if choice == "1":
            city_explorer()
        elif choice == "2":
            compare_cities()
        elif choice == "3":
            weather_explorer()
        elif choice == "q":
            print("Goodbye!")
            break
        else:
            print("Please choose 1, 2, 3, or Q.")


if __name__ == "__main__":
    main()
