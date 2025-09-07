from fastapi import APIRouter, Request
from app.core.startup import templates

router = APIRouter()

@router.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
