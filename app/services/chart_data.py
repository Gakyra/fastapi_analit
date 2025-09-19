import httpx
from loguru import logger

async def get_chart_data(asset_id: str, days: int = 7):
    url = f"https://api.coingecko.com/api/v3/coins/{asset_id}/market_chart"
    params = {
        "vs_currency": "usd",
        "days": days
    }

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            prices = data.get("prices", [])
            return [{"timestamp": ts, "price": p} for ts, p in prices]
    except Exception as e:
        logger.warning(f"Chart fetch failed for {asset_id}: {e}")
        return []
