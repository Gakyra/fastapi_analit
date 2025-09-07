from loguru import logger

class LLMProcessor:
    def __init__(self):
        logger.info("LLMProcessor initialized")

    async def analyze(self, query: str, asset: str, mode: str) -> str:
        logger.debug(f"Analyzing: query='{query}', asset='{asset}', mode='{mode}'")

        # Пример простой логики — можно заменить на вызов LLM или API
        if mode == "finance":
            return f"📈 Фінансовий аналіз для {asset}: {query}"
        elif mode == "psychology":
            return f"🧠 Психологічний розбір: {query}"
        elif mode == "forecast":
            return f"🔮 Прогноз для {asset}: {query}"
        else:
            return f"❓ Невідомий режим аналізу: {mode}"
