from fastapi import APIRouter, Request, Form
from fastapi.responses import RedirectResponse
from app.core.startup import templates

router = APIRouter()

# users_db: username → {email, password}
users_db = {}

@router.get("/register")
async def register_page(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@router.post("/register")
async def register(
    request: Request,
    username: str = Form(...),
    email: str = Form(...),
    password: str = Form(...)
):
    users_db[username] = {"email": email, "password": password}
    response = RedirectResponse("/", status_code=303)
    response.set_cookie(key="user", value=username)
    return response

@router.get("/login")
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@router.post("/login")
async def login(
    request: Request,
    identifier: str = Form(...),  # username or email
    password: str = Form(...)
):
    # Поиск по username
    user = users_db.get(identifier)
    if user and user["password"] == password:
        response = RedirectResponse("/", status_code=303)
        response.set_cookie(key="user", value=identifier)
        return response

    # Поиск по email
    for username, data in users_db.items():
        if data["email"] == identifier and data["password"] == password:
            response = RedirectResponse("/", status_code=303)
            response.set_cookie(key="user", value=username)
            return response

    return templates.TemplateResponse("login.html", {
        "request": request,
        "error": "Невірне ім’я користувача або email, або пароль"
    })

@router.get("/logout")
async def logout():
    response = RedirectResponse("/", status_code=303)
    response.delete_cookie("user")
    return response
