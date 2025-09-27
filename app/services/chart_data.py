import httpx, json, os
from loguru import logger

CACHE_DIR = "chart_cache"
os.makedirs(CACHE_DIR, exist_ok=True)

def load_chart_from_file(asset_id: str, days: int):
    path = f"{CACHE_DIR}/{asset_id}_{days}.json"
    if os.path.exists(path):
        try:
            with open(path, "r") as f:
                return json.load(f)
        except Exception as e:
            logger.warning(f"Failed to load chart from file: {e}")
    return []

def save_chart_to_file(asset_id: str, days: int, data):
    path = f"{CACHE_DIR}/{asset_id}_{days}.json"
    try:
        with open(path, "w") as f:
            json.dump(data, f)
    except Exception as e:
        logger.warning(f"Failed to save chart to file: {e}")

async def get_chart_data(asset_id: str, days: int = 30):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"https://api.coingecko.com/api/v3/coins/{asset_id}/market_chart",
                params={"vs_currency": "usd", "days": days}
            )
            response.raise_for_status()
            data = response.json()
            prices = data.get("prices", [])
            result = [{"timestamp": ts, "price": p} for ts, p in prices]

            if result:
                save_chart_to_file(asset_id, days, result)
                return result

    except Exception as e:
        logger.warning(f"Chart fetch failed for {asset_id}: {e}")

    # ✅ Fallback: возвращаем последний сохранённый график
    return load_chart_from_file(asset_id, days)
