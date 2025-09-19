from fastapi import FastAPI
from app.core.startup import setup_logging, setup_exception_handlers
from app.api.main import router as main_router
from app.api.analytics import router as analytics_router
from app.api.auth import router as auth_router
from app.api.history import router as history_router
from app.api.assets import router as assets_router
from app.api.asset_detail import router as asset_detail_router
from app.api.watchlist import router as watchlist_router


app = FastAPI(title="Інвест‑Аналітик")

# 🔧 Инициализация
setup_logging(app)
setup_exception_handlers(app)

# 🔗 Подключение роутов
app.include_router(main_router)
app.include_router(analytics_router, prefix="/analytics")
app.include_router(auth_router, prefix="/auth")
app.include_router(history_router, prefix="/analytics")
app.include_router(assets_router)
app.include_router(asset_detail_router)
app.include_router(watchlist_router)

