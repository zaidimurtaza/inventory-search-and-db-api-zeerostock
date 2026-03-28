from fastapi import FastAPI, HTTPException

from app.routes import supplier
from app.routes import inventory
from app.db import create_tables

app = FastAPI()

app.include_router(supplier.router)
app.include_router(inventory.router)

@app.on_event("startup")
def startup():
    create_tables()


@app.get("/")
def read_root():
    return {"message": "Hello, World! from part B"}
