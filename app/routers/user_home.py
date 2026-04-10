from fastapi import APIRouter, HTTPException, Depends, Request
from sqlmodel import select
from sqlalchemy.orm import selectinload
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi import status
from app.models.user import SignImage
from app.schemas.user import SignPublic
from app.dependencies.session import SessionDep
from app.dependencies.auth import AuthDep, IsUserLoggedIn, get_current_user, is_admin
from . import router, templates


@router.get("/app", response_class=HTMLResponse)
async def user_home_view(
    request: Request,
    user: AuthDep,
    db:SessionDep
):
    statement = select(SignImage).options(selectinload(SignImage.user))
    db_signs = db.exec(statement).all()

    signs = [SignPublic.model_validate(s) for s in db_signs] 

    return templates.TemplateResponse(
        request=request, 
        name="app.html",
        context={
            "user": user,
            "signs": signs,
        }
    )