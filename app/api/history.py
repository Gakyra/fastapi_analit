
from fastapi import APIRouter, Request
from app.core.startup import templates

router = APIRouter()

@router.get("/history")
async def history_page(request: Request):
    return templates.TemplateResponse("history.html", {"request": request})
