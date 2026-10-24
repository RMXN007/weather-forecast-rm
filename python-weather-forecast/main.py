import requests

GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
WEATHER_URL = "https://api.open-meteo.com/v1/forecast"


def get_city_coordinates(city):
    """Find a city's latitude and longitude."""

    response = requests.get(
        GEOCODING_URL,
        params={
            "name": city,
            "count": 1,
            "language": "en",
            "format": "json"
        },
        timeout=15
    )
    response.raise_for_status()

    data = response.json()
    results = data.get("results", [])

    if not results:
        print("City not found. Please check the spelling.")
        return None

    location = results[0]

    return {
        "name": location["name"],
        "country": location.get("country", "Unknown"),
        "latitude": location["latitude"],
        "longitude": location["longitude"]
    }


def get_weather(latitude, longitude):
    """Fetch current weather and a 7-day forecast."""

    response = requests.get(
        WEATHER_URL,
        params={
            "latitude": latitude,
            "longitude": longitude,
            "current": (
                "temperature_2m,"
                "relative_humidity_2m,"
                "apparent_temperature,"
                "weather_code,"
                "wind_speed_10m"
            ),
            "daily": (
                "weather_code,"
                "temperature_2m_max,"
                "temperature_2m_min,"
                "precipitation_probability_max"
            ),
            "timezone": "auto",
            "forecast_days": 7
        },
        timeout=20
    )

    response.raise_for_status()
    return response.json()


def describe_weather(code):
    """Convert weather codes into readable descriptions."""

    descriptions = {
        0: "Clear sky",
        1: "Mainly clear",
        2: "Partly cloudy",
        3: "Overcast",
        45: "Fog",
        48: "Depositing rime fog",
        51: "Light drizzle",
        53: "Moderate drizzle",
        55: "Dense drizzle",
        61: "Slight rain",
        63: "Moderate rain",
        65: "Heavy rain",
        71: "Slight snowfall",
        73: "Moderate snowfall",
        75: "Heavy snowfall",
        80: "Rain showers",
        81: "Moderate rain showers",
        82: "Violent rain showers",
        95: "Thunderstorm",
        96: "Thunderstorm with hail",
        99: "Thunderstorm with heavy hail"
    }

    return descriptions.get(code, "Unknown conditions")


def display_weather(location, data):
    """Display current weather and daily forecasts."""

    current = data["current"]
    daily = data["daily"]

    print("\n" + "=" * 45)
    print(f"WEATHER FORECAST: {location['name']}, "
          f"{location['country']}")
    print("=" * 45)

    print("\nCURRENT WEATHER")
    print("-" * 45)
    print(f"Temperature: {current['temperature_2m']} °C")
    print(f"Feels like: {current['apparent_temperature']} °C")
    print(f"Condition: "
          f"{describe_weather(current['weather_code'])}")
    print(f"Humidity: {current['relative_humidity_2m']}%")
    print(f"Wind speed: {current['wind_speed_10m']} km/h")
    print(f"Updated time: {current['time']}")

    print("\n7-DAY FORECAST")
    print("-" * 45)

    for i, date in enumerate(daily["time"]):
        condition = describe_weather(daily["weather_code"][i])
        maximum = daily["temperature_2m_max"][i]
        minimum = daily["temperature_2m_min"][i]
        rain = daily["precipitation_probability_max"][i]

        print(f"\nDate: {date}")
        print(f"Condition: {condition}")
        print(f"Max temperature: {maximum} °C")
        print(f"Min temperature: {minimum} °C")
        print(f"Maximum rain probability: {rain}%")


def main():
    print("=" * 45)
    print("       PYTHON WEATHER FORECAST")
    print("=" * 45)

    while True:
        city = input(
            "\nEnter city name (or type exit to quit): "
        ).strip()

        if city.lower() == "exit":
            print("Thank you for using Weather Forecast!")
            break

        if not city:
            print("Please enter a city name.")
            continue

        try:
            location = get_city_coordinates(city)

            if location is None:
                continue

            print(f"Fetching weather for {location['name']}...")

            weather_data = get_weather(
                location["latitude"],
                location["longitude"]
            )

            display_weather(location, weather_data)

        except requests.exceptions.Timeout:
            print("Request timed out. Please try again.")

        except requests.exceptions.ConnectionError:
            print("Connection failed. Check your internet.")

        except requests.exceptions.HTTPError as error:
            print("Weather API returned an error:", error)

        except (KeyError, ValueError) as error:
            print("Could not process weather data:", error)


if __name__ == "__main__":
    main()
