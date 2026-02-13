from typing import Optional
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware # Импортируем прослойку CORS

from api import get_data

app = FastAPI()

# Настройка CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/product-view/filters")
async def kaspi_data(category: Optional[str] = None):
    if category is None: return None
    return await get_data(category)

