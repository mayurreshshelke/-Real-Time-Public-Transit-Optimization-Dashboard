import requests
import os
from utils.config import GOOGLE_API_KEY

def fetch_transit_data(origin, destination):
    """
    Fetch real-time transit data between two points.
    """
    url = f"https://maps.googleapis.com/maps/api/directions/json"
    params = {
        "origin": origin,
        "destination": destination,
        "mode": "transit",
        "departure_time": "now",
        "key": GOOGLE_API_KEY
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

# Example usage
if __name__ == "__main__":
    origin = "Times Square, New York, NY"
    destination = "Central Park, New York, NY"
    data = fetch_transit_data(origin, destination)
    print(data)
