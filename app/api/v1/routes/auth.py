from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.auth import RegisterRequest, LoginRequest, TokenResponse
from app.services.auth_service import AuthService
from app.models.user import UserRole
from app.core.database import get_db

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register/{role}")
async def register(
    role: UserRole,
    payload: RegisterRequest,
    db: AsyncSession = Depends(get_db),
):
    service = AuthService(db)
    user = await service.register_user(
        email=payload.email,
        password=payload.password,
        role=role,
    )
    return {
        "id": user.id,
        "email": user.email,
        "role": user.role,
        "verified": user.is_verified,
    }


@router.post("/login", response_model=TokenResponse)
async def login(
    payload: LoginRequest,
    db: AsyncSession = Depends(get_db),
):
    service = AuthService(db)
    token, role = await service.login(payload.email, payload.password)
    return {"access_token": token, "role": role}
