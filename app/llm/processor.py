from loguru import logger

class LLMProcessor:
    def __init__(self):
        logger.debug("LLMProcessor initialized")

    async def analyze(self, query: str) -> str:
        logger.info(f"Analyzing query: {query}")

        # Мок-логика — можно заменить на вызов реального LLM
        query_lower = query.lower()

        if "инфляция" in query_lower:
            result = "Инфляция — ключевой фактор. Проверьте динамику за последние 12 месяцев."
        elif "экономика" in query_lower:
            result = "Обнаружены экономические термины. Рекомендуем углублённый анализ."
        elif "рецессия" in query_lower:
            result = "Рецессия может быть циклической. Проверьте макроэкономические индикаторы."
        else:
            result = f"Запрос принят: {query}. Пока нет специфических паттернов."

        logger.debug(f"LLM result: {result}")
        return result
