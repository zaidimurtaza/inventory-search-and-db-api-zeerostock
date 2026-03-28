from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from typing import Callable
import time
from fastapi.middleware.cors import CORSMiddleware

from app.routes.search import router as search_router


app = FastAPI()

app.include_router(search_router)


@app.get("/")
async def root():
    return {"message": "Hello, World!"}


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(status_code=exc.status_code, content={"message": exc.detail})

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_methods=["*"],
    allow_headers=["*"],
)