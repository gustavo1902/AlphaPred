import logging
import requests

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def fetch_polymarket_events():
    try:
        response = requests.get(POLYMARKET_API, timeout=10)
        response.raise_for_status() 
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Erro ao buscar dados da Polymarket: {e}")
        return []