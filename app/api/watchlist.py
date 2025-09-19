from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse
from app.core.startup import templates
from app.services.assets import ASSETS

router = APIRouter()
watchlist = set()

@router.get("/watchlist")
async def view_watchlist(request: Request):
    assets = [{"id": aid, "name": ASSETS[aid]} for aid in watchlist if aid in ASSETS]
    return templates.TemplateResponse("watchlist.html", {"request": request, "assets": assets})

@router.get("/watchlist/add/{asset_id}")
async def add_to_watchlist(asset_id: str):
    watchlist.add(asset_id)
    return RedirectResponse(f"/assets/{asset_id}", status_code=303)
