from app.db.session import SessionLocal
from app.db.models import QueryLog
from loguru import logger

async def save_query(query: str, result: str):
    async with SessionLocal() as session:
        log = QueryLog(query=query, result=result)
        session.add(log)
        await session.commit()
        logger.info("Query saved to DB")
