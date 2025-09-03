from fastapi import APIRouter, Request, Form
from fastapi.responses import RedirectResponse
from app.core.startup import templates
from app.llm.processor import LLMProcessor
from app.services.analytics import save_query
from loguru import logger

router = APIRouter()
llm = LLMProcessor()

@router.get("/view")
async def analytics_view(request: Request):
    logger.debug("GET /analytics/view — rendering form")
    return templates.TemplateResponse("analytics.html", {
        "request": request,
        "result": None,
        "error": None
    })

@router.post("/view")
async def analytics_post(request: Request, query: str = Form(...)):
    logger.info(f"POST /analytics/view — received query: {query}")

    try:
        result = await llm.analyze(query)
        logger.debug(f"LLM result: {result}")
        await save_query(query, result)
        logger.info("Query saved successfully")
        return templates.TemplateResponse("analytics.html", {
            "request": request,
            "result": result,
            "error": None
        })
    except Exception as e:
        logger.exception("Error during analytics processing")
        return templates.TemplateResponse("analytics.html", {
            "request": request,
            "result": None,
            "error": "Произошла ошибка при обработке запроса."
        })
