#!/bin/bash

# Weather Dashboard Startup Script

echo "🌤️  Starting Weather Dashboard..."
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Install requirements
echo "📥 Installing dependencies..."
pip install -r requirements.txt

# Check for API key
if [ -z "$OPENWEATHER_API_KEY" ] && [ ! -f ".env" ]; then
    echo ""
    echo "⚠️  WARNING: No API key configured!"
    echo "   Please set your OpenWeatherMap API key:"
    echo "   1. Set environment variable: export OPENWEATHER_API_KEY='your-key'"
    echo "   2. Or create .env file: cp .env.example .env (then edit it)"
    echo "   3. Or edit the API_KEY variable in app.py"
    echo ""
    echo "   Get your free API key at: https://openweathermap.org/api"
    echo ""
fi

# Start the application
echo "🚀 Starting the web server..."
echo "   Open http://localhost:5000 in your browser"
echo ""
python app.py
