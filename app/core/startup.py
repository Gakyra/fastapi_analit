from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from loguru import logger

templates = Jinja2Templates(directory="templates")

def setup_logging(app: FastAPI):
    logger.remove()
    logger.add("logs/app.log", rotation="1 MB", retention="10 days", level="DEBUG")
    logger.info("Logging initialized")

def setup_exception_handlers(app: FastAPI):
    @app.exception_handler(Exception)
    async def global_exception_handler(request, exc):
        logger.exception(f"Unhandled error: {exc}")
        return {"error": "Internal server error"}
