from fastapi import APIRouter, Request
from app.core.startup import templates
from app.services.chart_data import get_chart_data
from app.services.assets import ASSETS

router = APIRouter()

@router.get("/assets/{asset_id}")
async def asset_detail(request: Request, asset_id: str):
    if asset_id not in ASSETS:
        return templates.TemplateResponse("404.html", {"request": request})

    chart_7d = await get_chart_data(asset_id, days=7)
    chart_30d = await get_chart_data(asset_id, days=30)

    return templates.TemplateResponse("asset_detail.html", {
        "request": request,
        "asset_id": asset_id,
        "asset_name": ASSETS[asset_id],
        "chart_7d": chart_7d,
        "chart_30d": chart_30d
    })
