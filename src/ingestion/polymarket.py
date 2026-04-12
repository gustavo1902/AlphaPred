import logging
import requests
import json

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def fetch_polymarket_events():
    try:
        url = "https://gamma-api.polymarket.com/events?active=true&closed=false&limit=3"
        response = requests.get(url, timeout=10)
        response.raise_for_status() 
        events = response.json()
        
        formatted_events = []
        for event in events:
            if "markets" in event and len(event["markets"]) > 0:
                market = event["markets"][0]
                
                raw_prices = market.get("outcomePrices", '["0"]')
                
                if isinstance(raw_prices, str):
                    try:
                        prices_list = json.loads(raw_prices)
                    except json.JSONDecodeError:
                        prices_list = ["0"]
                else:
                    prices_list = raw_prices
                
                prob = float(prices_list[0]) if prices_list else 0.0
                
                formatted_events.append({
                    "id": market.get("id", "unknown"),
                    "question": event.get("title", "Unknown Event"),
                    "market_prob": prob,
                    "volume": float(market.get("volumeNum", 0)),
                    "source": "polymarket"
                })
                
        return formatted_events
        
    except requests.exceptions.RequestException as e:
        logger.error(f"Erro ao buscar dados da Polymarket: {e}")
        return []