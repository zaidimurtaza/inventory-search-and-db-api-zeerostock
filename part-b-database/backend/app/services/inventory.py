from app.db import execute_query
from app.models.inventory import InventoryCreate, InventoryGroupResponse, InventoryResponse
from app.models.supplier import SupplierResponse

def insert_inventory(inventory: InventoryCreate) -> InventoryResponse:
    query = "INSERT INTO inventory (supplier_id, product_name, quantity, price) VALUES (%s, %s, %s, %s) RETURNING id, supplier_id, product_name, quantity, price"
    params = (inventory.supplier_id, inventory.product_name, inventory.quantity, inventory.price)
    rows = execute_query(query, params)
    if not rows:
        raise RuntimeError("insert returned no row")
    row = rows[0]
    return InventoryResponse(id=row[0], supplier_id=row[1], product_name=row[2], quantity=row[3], price=row[4])


def get_inventory() -> list[InventoryGroupResponse]:
    query = """
        SELECT s.id, s.name, s.city,
               i.id, i.supplier_id, i.product_name, i.quantity, i.price
        FROM suppliers s
        JOIN inventory i ON s.id = i.supplier_id
        ORDER BY s.id
    """
    rows = execute_query(query) or []

    by_supplier: dict[int, InventoryGroupResponse] = {}
    for r in rows:
        if r[0] not in by_supplier:
            by_supplier[r[0]] = InventoryGroupResponse(
                supplier=SupplierResponse(id=r[0], name=r[1], city=r[2]),
                inventory=[],
                total_value=0,
            )
        item = InventoryResponse(id=r[3], supplier_id=r[4], product_name=r[5], quantity=r[6], price=r[7])
        by_supplier[r[0]].inventory.append(item)
        by_supplier[r[0]].total_value += r[6] * r[7]

    return sorted(by_supplier.values(), key=lambda x: x.total_value, reverse=True)