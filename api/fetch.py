from fastapi import HTTPException
from curl_cffi import requests

def get_data(category: str):
    url = 'https://kaspi.kz/yml/product-view/pl/filters'

    # Параметры запроса (Query Strings)
    params = {
        'q': f':category:{category}:availableInZones:Magnum_ZONE1',
        'text': '',
        'all': 'false',
        'sort': 'relevance',
        'ui': 'd',
        'i': '-1',
        'c': '750000000'
    }

    # Заголовки как в вашем браузере
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

    # Куки (помните, что они могут протухнуть через время)
    cookies = {
        "k_stat": "09de4cbe-9cf4-4708-a2e5-44de4e22d657",
        "ks.tg": "20",
        "kaspi.storefront.cookie.city": "750000000",
        "current-action-name": "Index",
        "locale": "ru-RU"
    }

    try:
        # Используем impersonate="chrome" для обхода защиты Kaspi
        response = requests.get(
            url,
            params=params,
            headers=headers,
            cookies=cookies,
            impersonate="chrome110",
            timeout=15
        )

        # Если статус не 200, выбрасываем ошибку
        if response.status_code != 200:
            # Если вернулся HTML вместо JSON, значит IP заблокирован
            if "text/html" in response.headers.get("Content-Type", ""):
                raise HTTPException(
                    status_code=403,
                    detail="Kaspi blocked Vercel IP. Try to change region or use proxy."
                )
            raise HTTPException(
                status_code=response.status_code,
                detail=f"Kaspi API error: {response.text[:500]}"
            )

        return response.json()

    except Exception as e:
        # Ловим системные ошибки (таймауты, отсутствие интернета и т.д.)
        if isinstance(e, HTTPException):
            raise e
        raise HTTPException(status_code=500, detail=f"Internal error: {str(e)}")