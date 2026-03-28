from app.db import execute_query
from app.models.supplier import SupplierCreate, SupplierResponse


def insert_supplier(supplier: SupplierCreate) -> SupplierResponse:
    query = "INSERT INTO suppliers (name, city) VALUES (%s, %s) RETURNING id, name, city"
    params = (supplier.name, supplier.city)
    rows = execute_query(query, params)
    if not rows:
        raise RuntimeError("insert returned no row")
    row = rows[0]
    return SupplierResponse(id=row[0], name=row[1], city=row[2])