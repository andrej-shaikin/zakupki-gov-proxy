from fastapi import APIRouter

from apps.contracts.routes import router as contract_routes

router = APIRouter()

router.include_router(
    router=contract_routes,
    prefix='/contracts',
    tags=['contracts', ],
)

__all__ = ["router"]
