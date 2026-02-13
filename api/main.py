from typing import Optional
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware # Импортируем прослойку CORS
import httpx

from .fetch import get_data

app = FastAPI()

# Настройка CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/api/product-view/filters")
async def kaspi_data(category: Optional[str] = None):
    if category is None: return None
    return await get_data(category)

@app.get("/check-ip")
async def check_ip():
    async with httpx.AsyncClient() as client:
        res = await client.get("https://api.ipify.org?format=json")
        return res.json()