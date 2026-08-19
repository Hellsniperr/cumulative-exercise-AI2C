import requests
from fastapi import FastAPI

app = FastAPI()

API_KEY = "6a85dbcc3a6bd548672721fehd58a24"
GEOCODE_URL = "https://geocode.maps.co/search"


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.post("/geocode/{city}/{state}")
def geocode(city: str, state: str):
    query = f"{city}, {state}"

    response = requests.get(
        GEOCODE_URL,
        params={"q": query, "api_key": API_KEY},
        timeout=5,
    )

    results = response.json()
    first_result = results[0]

    return {
        "lat": first_result["lat"],
        "long": first_result["lon"],
    }
