import os
import requests
from twilio.rest import Client

# --- CONFIGURATION KEYS ---
# (For security in production, it's best practice to use environment variables)
WEATHER_API_KEY = "YOUR_OPENWEATHERMAP_API_KEY"
CITY_NAME = "London"  # Replace with the host's city

TWILIO_ACCOUNT_SID = "YOUR_TWILIO_ACCOUNT_SID"
TWILIO_AUTH_TOKEN = "YOUR_TWILIO_AUTH_TOKEN"
TWILIO_PHONE_NUMBER = "YOUR_TWILIO_PHONE_NUMBER"  # Formatted like '+1234567890'
HOST_PHONE_NUMBER = "YOUR_HOST_PHONE_NUMBER"  # The recipient host's phone number


def get_weather_forecast(city, api_key):
    """Fetches real-time weather information using OpenWeatherMap API."""
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    # Using 'metric' gives Celsius. Switch to 'imperial' for Fahrenheit if needed.
    query_parameters = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    try:
        response = requests.get(base_url, params=query_parameters)
        response.raise_for_status()  # Check for HTTP request errors
        weather_data = response.json()

        # Parsing data out of the JSON response payload
        temperature = weather_data["main"]["temp"]
        feels_like = weather_data["main"]["feels_like"]
        weather_description = weather_data["weather"][0]["description"].capitalize()
        humidity = weather_data["main"]["humidity"]

        # Structuring the final text message layout
        sms_body = (
            f"Good Morning! Here is today's weather update for {city}:\n"
            f"• Condition: {weather_description}\n"
            f"• Temp: {temperature}°C (Feels like {feels_like}°C)\n"
            f"• Humidity: {humidity}%"
        )
        return sms_body

    except requests.exceptions.RequestException as error:
        print(f"Failed to fetch weather data: {error}")
        return None


def send_sms_to_host(message_content):
    """Dispatches the weather text message via Twilio API."""
    try:
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        sms_delivery = client.messages.create(
            body=message_content,
            from_=TWILIO_PHONE_NUMBER,
            to=HOST_PHONE_NUMBER
        )
        print(f"Success! SMS dispatched to host. Message SID: {sms_delivery.sid}")
    except Exception as error:
        print(f"An error occurred while attempting to send SMS: {error}")


if __name__ == "__main__":
    print("Retrieving weather updates...")
    forecast_report = get_weather_forecast(CITY_NAME, WEATHER_API_KEY)

    if forecast_report:
        print("\n--- Message Preview ---")
        print(forecast_report)
        print("-----------------------\n")

        print("Sending SMS to your host...")
        send_sms_to_host(forecast_report)
    else:
        print("Aborting SMS transmission due to empty weather data data.")