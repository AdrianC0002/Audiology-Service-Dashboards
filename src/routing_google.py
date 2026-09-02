"""
Google Routes API route-matrix helper.

Prototype only with synthetic locations.
For real patient/home locations, obtain company approval and use only an approved account.
"""

import os
import requests

ROUTES_URL = "https://routes.googleapis.com/distanceMatrix/v2:computeRouteMatrix"

def compute_matrix(origins, destinations, departure_time=None):
    key = os.getenv("GOOGLE_MAPS_API_KEY")
    if not key:
        raise RuntimeError("GOOGLE_MAPS_API_KEY is not set.")

    def wp(x):
        return {
            "waypoint": {
                "location": {
                    "latLng": {
                        "latitude": x["latitude"],
                        "longitude": x["longitude"],
                    }
                }
            }
        }

    body = {
        "origins": [wp(x) for x in origins],
        "destinations": [wp(x) for x in destinations],
        "travelMode": "DRIVE",
        "routingPreference": "TRAFFIC_AWARE",
    }
    if departure_time:
        body["departureTime"] = departure_time

    headers = {
        "Content-Type": "application/json",
        "X-Goog-Api-Key": key,
        "X-Goog-FieldMask":
            "originIndex,destinationIndex,distanceMeters,duration,status,condition"
    }

    response = requests.post(ROUTES_URL, json=body, headers=headers, timeout=60)
    response.raise_for_status()
    return response.json()
