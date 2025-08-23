import requests
import re
import streamlit as st

class CalculatorTool:
    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b
    
    def subtract(self, a, b):
        return a - b
    
    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero is not allowed."
        return a / b


class WeatherTool:
    def get_weather(self, city):
        api_key = st.secrets["tomorrow_io_key"]
        city = city.replace("?", "").strip()

        
        weather_codes = {
            1000: "Clear",
            1100: "Mostly Clear",
            1101: "Partly Cloudy",
            1102: "Mostly Cloudy",
            1001: "Cloudy",
            2000: "Fog",
            2100: "Light Fog",
            4000: "Drizzle",
            4001: "Rain",
            4200: "Light Rain",
            4201: "Heavy Rain",
            5000: "Snow",
            5001: "Flurries",
            5100: "Light Snow",
            5101: "Heavy Snow",
            6000: "Freezing Drizzle",
            # Add more codes as needed
        }
        
        url = f'https://api.tomorrow.io/v4/weather/realtime?location={city}&apikey={api_key}'
        
        try:
            response = requests.get(url)
            response.raise_for_status() 
            data = response.json()

            # Navigate the correct JSON structure for the 'realtime' endpoint
            temperature = data['data']['values']['temperature']
            weather_code = data['data']['values']['weatherCode']
            
            condition = weather_codes.get(weather_code, "Unknown")
            
            return f"The weather in {city} is {condition} with {temperature}°C."
            
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 401:
                return "Error: Unauthorized. Please check your Tomorrow.io API key."
            elif e.response.status_code == 400:
                return "Error: Could not find weather for that location."
            else:
                return f"An HTTP error occurred: {e}"
        except Exception:
            return "An error occurred while fetching weather data. Please check your query and API key."


class StringTool:
    def reverse_string(self, s):
        return s[::-1]

    def uppercase_string(self, s):
        return s.upper()
    
    def lowercase_string(self, s):
        return s.lower()
    
    def palindrome_check(self, s):
        cleaned = re.sub(r'[^A-Za-z0-9]', '', s).lower()
        return cleaned == cleaned[::-1]
    
    def count_vowels(self, s):
        return sum(1 for char in s.lower() if char in 'aeiou')
    
    def count_consonants(self, s):
        return sum(1 for char in s.lower() if char.isalpha() and char not in 'aeiou')
    


class UnitConversionTool:
    def convert_cm_to_m(self, amount):
        return amount / 100

    def convert_m_to_cm(self, amount):
        return amount * 100

    def convert_km_to_m(self, amount):
        return amount * 1000
    
    def convert_m_to_km(self, amount):
        return amount / 1000

    def convert_kg_to_g(self, amount):
        return amount * 1000

    def convert_g_to_kg(self, amount):
        return amount / 1000
    

