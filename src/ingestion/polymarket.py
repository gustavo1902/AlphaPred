import requests

POLYMARKET_API = "https://gamma-api.polymarket.com/markets"
def fetch_polymarket_events():
    response = requests.get(POLYMARKET_API)

    print("STATUS:", response.status_code)
    print("TEXT:", response.text[:500])  

    return []