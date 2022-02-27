import json
import os

import requests
from dotenv import load_dotenv

load_dotenv("./.env")

# api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}
# api.openweathermap.org/data/2.5/weather?lat=35&lon=139&appid={API key}

city = input("Input city name ")
SAVE_WEATHER_PATH = "weather.json"
TOKEN_WEATHER = os.getenv("WEATHER", 0)
RETRIEVING_WEATHER_URL = (
    "https://api.openweathermap.org/data/2.5/weather?q=city&appid=TOKEN_WEATHER"
)
print(RETRIEVING_WEATHER_URL)


def extract_weather_info(data):
    return data.get("_embedded", {}).get("artists", [])


def make_example_request(url, headers):
    r = None
    try:
        r = requests.get(url, headers=headers)
        # if r.status_code == 200
        r.raise_for_status()
        json_data = r.json()
        return json_data
    except Exception as e:
        print(e)
    return None


def pipeline(path):
    weather_data = []
    token = TOKEN_WEATHER

    headers = make_headers_for_api(token)
    data = make_example_request(RETRIEVING_WEATHER_URL, headers)

    weather_data.extend(extract_artists_info(data))

    next_url = extract_next_url(data)

    counter = 1
    while next_url:
        try:
            print(counter)
            data = make_example_request(RETRIEVING_ARTISTS_URL, headers)
            weather_data.extend(extract_weather_info(data))
            next_url = extract_next_url(data)
            counter += 1
            if counter > 2:
                break
        except Exception as e:
            print(e)
            break
    save_weather_info(weather_data, path)


if __name__ == "__main__":
    pipeline(SAVE_WEATHER_PATH_PATH)
