from fastapi import FastAPI
from app.core.startup import setup_logging, setup_exception_handlers, templates
from app.api.analytics import router as analytics_router

app = FastAPI(title="FastAPI Analit")

setup_logging(app)
setup_exception_handlers(app)

app.include_router(analytics_router, prefix="/analytics")

@app.get("/")
async def root():
    return {"message": "FastAPI Analit is running"}
