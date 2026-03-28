from fastapi import APIRouter
from app.db.schema import create_tables
from app.models.supplier import SupplierCreate, SupplierResponse
from app.services.supplier import insert_supplier
from app.services.inventory import get_inventory


router = APIRouter(prefix='/supplier', tags=['supplier'])

@router.get("/")
def get_inventory():
    return get_inventory()


@router.post("/", response_model=SupplierResponse)
def create_supplier(supplier: SupplierCreate):
    return insert_supplier(supplier)