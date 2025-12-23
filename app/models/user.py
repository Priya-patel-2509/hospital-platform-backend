from sqlalchemy import String,Boolean,Enum
from enum import Enum as PyEnum
from sqlalchemy.orm import Mapped, mapped_column
from app.models.base import Base

class UserRole(PyEnum):
    PATIENT="patient"
    DOCTOR="doctor"
    ADMIN="admin"
    LAB_STAFF = "lab_staff"
    PHARMACY_SELLER = "pharmacy_seller"

class User(Base):
    __tablename__="users"

    id:Mapped[int]=mapped_column(primary_key=True)

    email:Mapped[str]=mapped_column(String(255),unique=True,index=True,nullable=False)

    password_hash: Mapped[str]=mapped_column(nullable=False)

    role:Mapped[UserRole]=mapped_column(Enum(UserRole),nullable=False)

    is_active:Mapped[bool]=mapped_column(
        Boolean,
        default=True
    )

    is_verified:Mapped[bool]=mapped_column(Boolean,default=False)

