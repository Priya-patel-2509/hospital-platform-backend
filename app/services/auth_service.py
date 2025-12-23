from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.user_repo import UserRepository
from app.utils.hashing import hash_password, verify_password
from app.utils.tokens import create_access_token
from app.models.user import User, UserRole
from app.core.role_policy import ROLE_POLICIES


class AuthService:
    def __init__(self, db: AsyncSession):
        self.repo = UserRepository(db)

    async def register_user(self, email: str, password: str, role: UserRole):
        if role not in ROLE_POLICIES:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid role",
            )

        if await self.repo.get_by_email(email):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Email already exists",
            )

        policy = ROLE_POLICIES[role]

        user = User(
            email=email,
            password_hash=hash_password(password),
            role=role,
            is_verified=policy["verified_by_default"],
        )

        return await self.repo.create_user(user)

    async def login(self, email: str, password: str):
        user = await self.repo.get_by_email(email)

        if not user or not verify_password(password, user.password_hash):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid credentials",
            )

        if not user.is_active:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="User disabled",
            )

        token = create_access_token(
            {"sub": str(user.id), "role": user.role.value}
        )

        return token, user.role
