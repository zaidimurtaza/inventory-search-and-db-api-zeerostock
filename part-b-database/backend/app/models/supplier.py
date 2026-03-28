from pydantic import BaseModel, Field



class SupplierResponse(BaseModel):
    id: int
    name: str
    city: str


class SupplierCreate(BaseModel):
    name: str
    city: str
