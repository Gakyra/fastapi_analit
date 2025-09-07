from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from loguru import logger
import os

templates = Jinja2Templates(directory="templates")

def setup_logging(app: FastAPI):
    os.makedirs("logs", exist_ok=True)
    logger.remove()
    logger.add("logs/app.log", rotation="1 MB", retention="10 days", level="DEBUG")
    logger.info("✅ Logging initialized")

def setup_exception_handlers(app: FastAPI):
    @app.exception_handler(Exception)
    async def global_exception_handler(request: Request, exc: Exception):
        logger.exception(f"❌ Unhandled error: {exc}")
        return JSONResponse(status_code=500, content={"error": "Internal server error"})
