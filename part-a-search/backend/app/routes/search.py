from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import JSONResponse

from app.search_service import search_products

router = APIRouter(prefix="/search", tags=["search"])


@router.get("/")
async def search(
    q: str | None = None,
    category: str | None = None,
    min_price: float | None = Query(None, alias="minPrice", ge=0),
    max_price: float | None = Query(None, alias="maxPrice", ge=0),
):
    if min_price is not None and max_price is not None and min_price > max_price:
        raise HTTPException(
            status_code=400,
            detail="Invalid price range: minPrice cannot be greater than maxPrice",
        )

    products = await search_products(q, category, min_price, max_price)

    return JSONResponse(
        status_code=200,
        content={"products": products},
    )