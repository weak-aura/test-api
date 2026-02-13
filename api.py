from fastapi import HTTPException
import httpx

async def get_data(category):
    url = 'https://kaspi.kz/yml/product-view/pl/filters'

    params = {
        'q': f':category:{category}:availableInZones:Magnum_ZONE1',
        'text': '',
        'all': 'false',
        'sort': 'relevance',
        'ui': 'd',
        'i': '-1',
        'c': '750000000'
    }

    headers = {
        'Accept': 'application/json, text/*',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'Referer': 'https://kaspi.kz/shop/c/categories/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36',
    }

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, params=params, headers=headers, timeout=10.0)
            response.raise_for_status()
            return response.json()

        except httpx.HTTPStatusError as e:
            raise HTTPException(status_code=e.response.status_code, detail=f"Kaspi API error: {e.response.text}")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Internal error: {str(e)}")


