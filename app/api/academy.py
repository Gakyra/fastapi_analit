from fastapi import APIRouter, Request
from app.core.startup import templates

router = APIRouter()

@router.get("/academy")
async def academy_page(request: Request):
    return templates.TemplateResponse("academy.html", {"request": request})
