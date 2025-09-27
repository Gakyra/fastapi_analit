from fastapi import APIRouter, Request, Form
from app.core.startup import templates
from app.services.assets import ASSETS, fetch_asset_data, get_type
from app.services.chart_data import get_chart_data

router = APIRouter()

@router.get("/view")
async def analytics_form(request: Request):
    return templates.TemplateResponse("analytics_form.html", {
        "request": request,
        "assets": ASSETS
    })

@router.post("/view")
async def analytics_result(request: Request, asset_id: str = Form(...)):
    asset_data = await fetch_asset_data()
    selected = next((a for a in asset_data if a["id"] == asset_id), None)
    chart_30d = await get_chart_data(asset_id, days=30)

    return templates.TemplateResponse("analytics_result.html", {
        "request": request,
        "asset": selected,
        "chart_30d": chart_30d,
        "asset_name": ASSETS.get(asset_id),
        "asset_type": get_type(asset_id)
    })
