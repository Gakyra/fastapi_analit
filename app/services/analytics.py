from app.db.session import async_session
from app.db.models import AnalyticsQuery
from loguru import logger

async def save_query(query: str, result: str, asset: str, mode: str):
    async with async_session() as session:
        try:
            entry = AnalyticsQuery(
                query=query,
                result=result,
                asset=asset,
                mode=mode
            )
            session.add(entry)
            await session.commit()
            logger.info("Запит збережено в базу")
        except Exception as e:
            logger.exception("Помилка при збереженні запиту")
