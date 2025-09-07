from fastapi import APIRouter, Request, Form
from app.core.startup import templates
from app.llm.processor import LLMProcessor
from app.services.analytics import save_query
from loguru import logger

router = APIRouter()
llm = LLMProcessor()

@router.get("/view")
async def analytics_view(request: Request):
    return templates.TemplateResponse("analytics.html", {
        "request": request,
        "result": None,
        "error": None
    })

@router.post("/view")
async def analytics_post(
    request: Request,
    query: str = Form(...),
    asset: str = Form(...),
    mode: str = Form(...)
):
    logger.info(f"Запит: {query} | Актив: {asset} | Тип: {mode}")

    try:
        result = await llm.analyze(query=query, asset=asset, mode=mode)
        await save_query(query=query, result=result, asset=asset, mode=mode)
        return templates.TemplateResponse("analytics.html", {
            "request": request,
            "result": result,
            "error": None
        })
    except Exception as e:
        logger.exception("Помилка при обробці запиту")
        return templates.TemplateResponse("analytics.html", {
            "request": request,
            "result": None,
            "error": "Виникла помилка при аналізі."
        })
