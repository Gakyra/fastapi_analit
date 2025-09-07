from fastapi import APIRouter, Request
from app.core.startup import templates

router = APIRouter()

@router.get("/assets")
async def assets_page(request: Request):
    assets_data = [
        {"name": "Bitcoin (BTC)", "type": "Crypto", "price": 108697.05, "change": -0.88},
        {"name": "Apple (AAPL)", "type": "Stock", "price": 239.69, "change": -0.04},
        {"name": "Memecoin (MEME)", "type": "Meme", "price": 0.00292, "change": +1.67}
    ]
    return templates.TemplateResponse("assets.html", {
        "request": request,
        "assets": assets_data
    })
