# Python Weather Forecast System

## Project Overview

**Python Weather Forecast System** is a command-line application that displays
weather information for any city entered by the user. The application uses the
free [Open-Meteo](https://open-meteo.com/) services to:

1. Find a city's latitude and longitude from its name.
2. Retrieve the current weather for that location.
3. Display a seven-day weather forecast.

The program is built with Python and uses HTTP requests to communicate with
online REST APIs. It does not require an API key.

## Features

- Search for a city by name.
- Display the city and country identified by the geocoding service.
- Show current:
  - Temperature
  - Feels-like temperature
  - Weather condition
  - Relative humidity
  - Wind speed
  - Data update time
- Show a seven-day forecast containing:
  - Date
  - Weather condition
  - Maximum temperature
  - Minimum temperature
  - Maximum probability of precipitation
- Convert Open-Meteo weather codes into readable descriptions.
- Handle invalid city names, empty input, network failures, timeouts, HTTP
  errors, and unexpected API data.
- Continue searching for another city until the user enters `exit`.

## Technologies Used

- **Python 3**
- **Requests** - Sends HTTP requests and processes API responses.
- **Open-Meteo Geocoding API** - Converts a city name into geographical
  coordinates.
- **Open-Meteo Forecast API** - Provides current conditions and daily forecast
  data.

## Project Structure

```text
python-weather-forecast/
├── main.py
├── requirements.txt
└── README.md
```

### `main.py`

The main Python file contains the complete application:

- `get_city_coordinates(city)` searches for a city and returns its location.
- `get_weather(latitude, longitude)` retrieves current weather and seven days
  of forecast data.
- `describe_weather(code)` converts WMO weather codes to readable text.
- `display_weather(location, data)` prints the weather report.
- `main()` manages user input, repeated searches, and error handling.

### `requirements.txt`

Lists the external Python dependency required by the project:

```text
requests
```

## How the Application Works

When the program starts, it asks the user to enter a city name.

1. The city name is sent to the Open-Meteo Geocoding API.
2. The first matching result provides the city name, country, latitude, and
   longitude.
3. Those coordinates are sent to the Open-Meteo Forecast API.
4. The API returns current weather and daily forecast data in JSON format.
5. The application converts weather codes into descriptions and prints a
   formatted report in the terminal.
6. The user can enter another city or type `exit` to close the program.

All temperatures are displayed in degrees Celsius, wind speed is displayed in
kilometres per hour, and the forecast timezone is selected automatically for
the requested location.

## Installation and Setup

### 1. Open the project directory

In PowerShell or Command Prompt, move into the project folder:

```powershell
cd "python-weather-forecast"
```

### 2. Create a virtual environment (recommended)

```powershell
python -m venv .venv
```

Activate it in PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

On Command Prompt, use:

```bat
.venv\Scripts\activate
```

### 3. Install the dependency

```powershell
python -m pip install -r requirements.txt
```

### 4. Run the application

```powershell
python main.py
```

## Example Usage

```text
=============================================
       PYTHON WEATHER FORECAST
=============================================

Enter city name (or type exit to quit): Pune
Fetching weather for Pune...

=============================================
WEATHER FORECAST: Pune, India
=============================================

CURRENT WEATHER
---------------------------------------------
Temperature: 28.4 °C
Feels like: 30.1 °C
Condition: Partly cloudy
Humidity: 62%
Wind speed: 10.2 km/h
```

The exact values and forecast depend on the current weather returned by
Open-Meteo.

## Error Handling

The application provides user-friendly messages for common problems:

- **City not found:** asks the user to check the spelling.
- **Empty input:** asks the user to enter a city name.
- **Timeout:** suggests trying the request again.
- **Connection failure:** asks the user to check their internet connection.
- **HTTP/API error:** reports that the weather service returned an error.
- **Invalid response data:** reports that the weather data could not be
  processed.

## Learning Outcomes

This project demonstrates:

- Writing a Python command-line application.
- Taking and validating user input.
- Sending GET requests with the `requests` library.
- Working with REST APIs and JSON data.
- Using geographical coordinates to request location-based data.
- Processing lists of daily forecast values.
- Mapping numeric weather codes to readable descriptions.
- Handling network and data-processing exceptions.

## Possible Future Improvements

- Add a graphical user interface or web interface.
- Allow the user to choose Celsius or Fahrenheit.
- Display weather icons.
- Add hourly forecasts.
- Save and compare weather reports for multiple cities.
- Add automated tests for API responses and weather-code conversion.
- Cache recent searches to reduce repeated API requests.

## Author

**Raman Pawar**

## License

This project is intended for educational use. Weather data is provided by
[Open-Meteo](https://open-meteo.com/).
