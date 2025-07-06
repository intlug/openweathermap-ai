#!/usr/bin/env python3
"""
Simple test script for OpenWeatherMap One Call API 3.0
"""

import requests
import json
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

API_KEY = os.getenv('OPENWEATHER_API_KEY', 'YOUR_API_KEY_HERE')
BASE_URL = "https://api.openweathermap.org/data/3.0/onecall"

def test_api(city_name="London"):
    """Test the OpenWeatherMap API with a sample city"""
    
    if API_KEY == 'YOUR_API_KEY_HERE':
        print("❌ Error: Please set your OpenWeatherMap API key!")
        print("   Set environment variable: export OPENWEATHER_API_KEY='your-key'")
        print("   Or create .env file with: OPENWEATHER_API_KEY=your-key")
        return
    
    print(f"🌍 Testing OpenWeatherMap API for {city_name}...")
    
    # First get coordinates for the city
    geocoding_url = "http://api.openweathermap.org/geo/1.0/direct"
    geo_params = {
        'q': city_name,
        'limit': 1,
        'appid': API_KEY
    }
    
    try:
        print(f"📍 Getting coordinates for {city_name}...")
        geo_response = requests.get(geocoding_url, params=geo_params)
        geo_response.raise_for_status()
        geo_data = geo_response.json()
        
        if not geo_data:
            print(f"❌ City '{city_name}' not found!")
            return
        
        lat = geo_data[0]['lat']
        lon = geo_data[0]['lon']
        actual_city = geo_data[0]['name']
        country = geo_data[0].get('country', 'Unknown')
        
        print(f"✅ Found: {actual_city}, {country} ({lat}, {lon})")
        
        # Now get weather data
        print("🌤️  Fetching weather data...")
        weather_params = {
            'lat': lat,
            'lon': lon,
            'appid': API_KEY,
            'units': 'metric',
            'exclude': 'minutely,alerts'
        }
        
        weather_response = requests.get(BASE_URL, params=weather_params)
        weather_response.raise_for_status()
        weather_data = weather_response.json()
        
        # Display current weather
        current = weather_data['current']
        print(f"\n🌡️  Current Weather in {actual_city}:")
        print(f"   Temperature: {current['temp']:.1f}°C (feels like {current['feels_like']:.1f}°C)")
        print(f"   Description: {current['weather'][0]['description'].title()}")
        print(f"   Humidity: {current['humidity']}%")
        print(f"   Wind Speed: {current['wind_speed']} m/s")
        print(f"   Pressure: {current['pressure']} hPa")
        
        # Display forecast
        print(f"\n📅 5-Day Forecast:")
        for i, day in enumerate(weather_data['daily'][:5]):
            from datetime import datetime
            date = datetime.fromtimestamp(day['dt']).strftime('%A, %B %d')
            temp_min = day['temp']['min']
            temp_max = day['temp']['max']
            desc = day['weather'][0]['description'].title()
            print(f"   {date}: {temp_min:.1f}°C - {temp_max:.1f}°C, {desc}")
        
        print(f"\n✅ API test completed successfully!")
        print(f"   You can now run the web application with: python app.py")
        
    except requests.exceptions.RequestException as e:
        print(f"❌ API request failed: {e}")
    except KeyError as e:
        print(f"❌ Unexpected API response format: {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

if __name__ == "__main__":
    import sys
    
    city = "London"  # Default city
    if len(sys.argv) > 1:
        city = " ".join(sys.argv[1:])
    
    test_api(city)
