from fastapi import Depends, HTTPException, status
from app.dependencies.auth import get_current_user
from app.models.user import UserRole


def require_role(role: UserRole):
    async def checker(user=Depends(get_current_user)):
        if user.get("role") != role.value:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Permission denied",
            )
        return user

    return checker
