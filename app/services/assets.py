import httpx
from loguru import logger

COINGECKO_API = "https://api.coingecko.com/api/v3/simple/price"

ASSETS = {
    "bitcoin": "Bitcoin (BTC)",
    "ethereum": "Ethereum (ETH)",
    "dogecoin": "Dogecoin (DOGE)",
    "pepe": "Pepe (MEME)",
    "solana": "Solana (SOL)",
    "cardano": "Cardano (ADA)",
    "ripple": "Ripple (XRP)",
    "litecoin": "Litecoin (LTC)",
    "shiba-inu": "Shiba Inu (SHIB)",
    "chainlink": "Chainlink (LINK)",
    "avalanche-2": "Avalanche (AVAX)",
    "tron": "TRON (TRX)",
    "uniswap": "Uniswap (UNI)",
    "polkadot": "Polkadot (DOT)",
    "stellar": "Stellar (XLM)",
    "binancecoin": "BNB (Binance)"
}

last_successful_data = []

def get_type(asset_id: str) -> str:
    if asset_id in ["pepe", "shiba-inu", "dogecoin"]:
        return "Meme"
    return "Crypto"

async def fetch_asset_data():
    global last_successful_data

    ids = ",".join(ASSETS.keys())
    params = {
        "ids": ids,
        "vs_currencies": "usd",
        "include_24hr_change": "true"
    }

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(COINGECKO_API, params=params)
            response.raise_for_status()
            data = response.json()

        result = []
        for asset_id, display_name in ASSETS.items():
            asset = data.get(asset_id)
            if asset:
                result.append({
                    "name": display_name,
                    "price": asset["usd"],
                    "change": round(asset.get("usd_24h_change", 0), 2),
                    "type": get_type(asset_id)
                })

        last_successful_data = result
        return result

    except Exception as e:
        logger.warning(f"CoinGecko API failed: {e}")
        return last_successful_data
