from app.models.user import UserRole

ROLE_POLICIES = {
    UserRole.PATIENT: {
        "verified_by_default": True,
    },
    UserRole.DOCTOR: {
        "verified_by_default": False,
    },
    UserRole.ADMIN: {
        "verified_by_default": True,
    },
    UserRole.LAB_STAFF: {
        "verified_by_default": False,
    },
    UserRole.PHARMACY_SELLER: {
        "verified_by_default": False,
    },
}
