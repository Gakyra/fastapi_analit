from fastapi import APIRouter, Request
from app.core.startup import templates
from app.services.assets import fetch_asset_data

router = APIRouter()

@router.get("/assets")
async def assets_page(request: Request):
    assets = await fetch_asset_data()
    return templates.TemplateResponse("assets.html", {
        "request": request,
        "assets": assets
    })
