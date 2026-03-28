import json
from pathlib import Path
from typing import Optional

_DATA_FILE = Path(__file__).resolve().parent / "data.json"

_products: Optional[list] = None


async def load_products() -> list:
    global _products
    if _products is None:
        with open(_DATA_FILE, encoding="utf-8") as f:
            _products = json.load(f)
    return _products


async def search_products(
    q: str | None = None,
    category: str | None = None,
    min_price: float | None = None,
    max_price: float | None = None,
) -> list:
    products = await load_products()
    results = list(products)

    if q is not None and q.strip():
        name = q.lower()
        results = [p for p in results if name in p["name"].lower()]
    if category is not None and category.strip():
        cat = category.lower()
        results = [p for p in results if p["category"].lower() == cat]
    if min_price is not None:
        results = [p for p in results if p["price"] >= min_price]
    if max_price is not None:
        results = [p for p in results if p["price"] <= max_price]

    return results