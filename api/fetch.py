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
        "accept": "application/json, text/*",
        "accept-language": "ru-RU,ru;q=0.9",
        "sec-ch-ua": '"Not(A:Brand";v="8", "Chromium";v="144", "Google Chrome";v="144"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "x-description-enabled": "true",
        "x-ks-city": "750000000",
        "Referer": "https://kaspi.kz/shop/c/fashion/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36"
    }

    cookies = {
        "k_stat": "09de4cbe-9cf4-4708-a2e5-44de4e22d657",
        "ks.tg": "20",
        "kaspi.storefront.cookie.city": "750000000",
        "current-action-name": "Index",
        "locale": "ru-RU"
    }

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, params=params, headers=headers, cookies=cookies, timeout=10.0)
            response.raise_for_status()
            return response.json()

        except httpx.HTTPStatusError as e:
            raise HTTPException(status_code=e.response.status_code, detail=f"Kaspi API error: {e.response.text}")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Internal error: {str(e)}")



# curl 'https://kaspi.kz/yml/product-view/pl/filters?q=%3AavailableInZones%3AMagnum_ZONE1%3Acategory%3AFashion&text&all=false&sort=relevance&ui=d&i=-1&c=750000000' \
#   -H 'Accept: application/json, text/*' \
#   -H 'Accept-Language: ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7' \
#   -H 'Connection: keep-alive' \
#   -b 'k_stat=09de4cbe-9cf4-4708-a2e5-44de4e22d657; ks.tg=20; kaspi.storefront.cookie.city=750000000; current-action-name=Index; locale=ru-RU; _hjSessionUser_283363=eyJpZCI6IjIxMTJjZjhjLTY3ZTAtNTMwYS1iMGEzLWQ2MTAxNTBiYTFlYiIsImNyZWF0ZWQiOjE3NzAzOTY1NDIyNzMsImV4aXN0aW5nIjp0cnVlfQ==' \
#   -H 'Referer: https://kaspi.kz/shop/c/fashion/?q=%3Acategory%3AFashion%3AavailableInZones%3AMagnum_ZONE1&sort=relevance&sc=' \
#   -H 'Sec-Fetch-Dest: empty' \
#   -H 'Sec-Fetch-Mode: cors' \
#   -H 'Sec-Fetch-Site: same-origin' \
#   -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36' \
#   -H 'X-Description-Enabled: true' \
#   -H 'X-KS-City: 750000000' \
#   -H 'sec-ch-ua: "Not(A:Brand";v="8", "Chromium";v="144", "Google Chrome";v="144"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "Windows"'