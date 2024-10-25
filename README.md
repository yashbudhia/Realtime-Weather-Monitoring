# Realtime Weather Monitoring App

## Table of Contents
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Project Setup](#project-setup)
5. [Design Choices](#design-choices)
6. [Directory Structure](#directory-structure)
7. [Usage](#usage)
8. [API Endpoints](#api-endpoints)
9. [Future Enhancements](#future-enhancements)

## Project Overview
The **Realtime Weather Monitoring App** is designed to provide users with real-time weather data for various cities, including current weather conditions, temperature, and forecasts. It features an intuitive interface that allows users to set temperature thresholds for alerts and visualize data through graphs.

## Features
- **Real-time Weather Data**: Fetch current weather conditions from the Weatherstack API.
- **Daily Summaries**: Display daily weather aggregates such as average, maximum, and minimum temperatures.
- **Temperature Unit Toggle**: Users can switch between Celsius and Fahrenheit for temperature readings.
- **Forecast Modal**: Provides detailed forecast data for each city.
- **Temperature Alert Thresholds**: Users can set customizable thresholds for temperature alerts.
- **Responsive Charts**: Visualize temperature changes throughout the day using Chart.js.

## Technologies Used
- **Backend**: Python with Flask for the server-side application.
- **Database**: MongoDB for storing weather data and user configurations.
- **Frontend**: HTML, CSS, and JavaScript (with Chart.js) for the user interface.
- **API Integration**: Weatherstack API for fetching real-time weather data.

## Project Setup
To set up the project locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd weather-monitoring-app
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up MongoDB**: Make sure you have MongoDB running and configure the connection in the `database/__init__.py` file.

5. **Run the Flask Application**:
   ```bash
   python app.py
   ```

6. **Access the Application**: Open your web browser and go to `http://127.0.0.1:5000` to access the application.

## Design Choices

- **Modular Architecture**: The application is organized into modules (weather, database, etc.) for better maintainability and separation of concerns.
- **RESTful API Design**: The backend exposes RESTful endpoints for retrieving weather data and settings, promoting a clear and intuitive interface.
- **Responsive Design**: The frontend is designed to be responsive, ensuring usability across different devices and screen sizes.

## Directory Structure

```
weather-monitoring-app/
│
├── app.py                # Main entry point for the Flask application
├── config.py             # Configuration file for API keys and scheduling interval
├── weather/              # Weather module for API integration and data processing
│   ├── __init__.py       # Initialize the module
│   ├── api.py            # Code for interacting with the Weatherstack API
│   ├── processor.py      # Code for processing weather data (aggregation, rollups)
│   ├── scheduler.py      # Scheduling API calls at regular intervals
│   ├── alert.py          # Logic for handling threshold-based alerts
│
├── database/             # MongoDB integration
│   ├── __init__.py       # Initialize MongoDB connection
│   ├── models.py         # Define MongoDB collections (weather data, summaries, alerts)
│
├── templates/            # HTML files for the frontend
│   └── index.html        # Main frontend UI
├── static/               # Static files like CSS, JS for the frontend
│   └── style.css         # Styles for the frontend
├── requirements.txt      # Python dependencies
└── README.md             # Documentation
```

## Usage

- **Accessing Weather Data**: Users can view the current weather data for different cities, along with graphs that display daily temperature changes.
- **Setting Temperature Alerts**: Users can configure alert thresholds, and the app will notify them when temperatures exceed these limits.
- **Viewing Forecasts**: Clicking the "Get Forecast" button will display a modal with detailed forecast data for the selected city.

## API Endpoints

- `GET /weather/current`: Retrieves current weather data for specified cities.
- `GET /weather/forecast?city=<city_name>`: Fetches forecast data for the specified city.
- `POST /set_threshold`: Updates the temperature alert threshold based on user input.

## Future Enhancements

- **User Authentication**: Implement user accounts to save personalized settings and preferences.
- **Mobile App**: Develop a mobile application version of the weather monitoring system.
- **More Data Visualizations**: Include additional graphs and data representations for better insights.