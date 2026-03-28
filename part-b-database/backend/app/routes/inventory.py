from fastapi import APIRouter
from app.models.inventory import InventoryCreate, InventoryResponse
from app.services.inventory import insert_inventory, get_inventory


router = APIRouter(prefix='/inventory', tags=['inventory'])

@router.get("/")
def get_inventory_groups():
    return get_inventory()


@router.post("/", response_model=InventoryResponse)
def create_inventory(inventory: InventoryCreate):
    return insert_inventory(inventory)