from decimal import Decimal

from pydantic import BaseModel, Field

from app.models.supplier import SupplierResponse


class InventoryResponse(BaseModel):
    id: int
    supplier_id: int
    product_name: str
    quantity: int = Field(..., ge=0)
    price: Decimal = Field(..., ge=0)


class InventoryCreate(BaseModel):
    supplier_id: int
    product_name: str
    quantity: int = Field(..., ge=0)
    price: Decimal = Field(..., ge=0)


class InventoryGroupResponse(BaseModel):
    supplier: SupplierResponse
    total_value: Decimal
    inventory: list[InventoryResponse]