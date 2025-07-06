# Weather Dashboard

A beautiful web application that displays current weather and 5-day forecast using the OpenWeatherMap One Call API 3.0.

## Features

- **Current Weather**: Temperature, feels like, humidity, wind speed, and weather description
- **5-Day Forecast**: Daily overview with min/max temperatures, weather conditions, humidity, and wind
- **24-Hour Forecast**: Hourly temperature and weather conditions for the next 24 hours
- **Beautiful UI**: Modern, responsive design with gradient backgrounds and animations
- **City Search**: Enter any city name to get weather information
- **API Endpoint**: RESTful API endpoint for programmatic access

## Prerequisites

- Python 3.7 or higher
- OpenWeatherMap API key (free at https://openweathermap.org/api)

## Installation

1. **Clone or download the project files**

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Get your OpenWeatherMap API key**:
   - Go to https://openweathermap.org/api
   - Sign up for a free account
   - Subscribe to the "One Call API 3.0" (free tier available)
   - Copy your API key

4. **Configure your API key**:
   
   **Option 1: Environment Variable (Recommended)**
   ```bash
   export OPENWEATHER_API_KEY="your_actual_api_key_here"
   ```
   
   **Option 2: Create .env file**
   ```bash
   cp .env.example .env
   # Edit .env file and replace 'AddYourAPIKeyHere' with your actual API key
   ```
   
   **Option 3: Edit app.py directly**
   - Open `app.py`
   - Replace `'YOUR_API_KEY_HERE'` with your actual API key

## Usage

1. **Start the application**:
   ```bash
   python app.py
   ```

2. **Open your web browser** and go to: http://localhost:5000

3. **Search for weather**:
   - Enter a city name in the search box
   - Click "Get Weather" to see current conditions and forecast

## API Endpoint

The application also provides a RESTful API endpoint:

```
GET /api/weather/<latitude>/<longitude>
```

Example:
```
http://localhost:5000/api/weather/40.7128/-74.0060
```

Returns JSON data with current weather, daily forecast, and hourly forecast.

## Features Explained

### Current Weather Display
- Large temperature display with weather icon
- "Feels like" temperature
- Humidity percentage
- Wind speed in meters per second
- Weather description
- Current date and time

### 5-Day Forecast
- Each day shows:
  - Date (day name and date)
  - Weather icon and description
  - High and low temperatures
  - Humidity and wind speed

### 24-Hour Forecast
- Hourly breakdown showing:
  - Time
  - Temperature
  - Weather icon
  - Scrollable container for easy viewing

### Responsive Design
- Works on desktop, tablet, and mobile devices
- Modern gradient backgrounds
- Smooth animations and hover effects
- Bootstrap-based responsive layout

## Troubleshooting

1. **"Please set your OpenWeatherMap API key!" message**:
   - Make sure you've set your API key using one of the methods above
   - Verify your API key is correct and active

2. **"City not found" error**:
   - Check the spelling of the city name
   - Try using the format "City, Country" (e.g., "London, UK")

3. **"Failed to fetch weather data" error**:
   - Check your internet connection
   - Verify your API key is valid and has One Call API 3.0 access
   - Make sure you haven't exceeded your API rate limits

## API Rate Limits

The free OpenWeatherMap plan includes:
- 1,000 API calls per day
- 60 calls per minute

## Technologies Used

- **Backend**: Python Flask
- **Frontend**: HTML5, CSS3, Bootstrap 5, Font Awesome
- **API**: OpenWeatherMap One Call API 3.0
- **HTTP Client**: Python requests library

## License

This project is open source and available under the MIT License.
