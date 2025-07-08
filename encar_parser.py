from playwright.async_api import async_playwright

async def fetch_recent_cars():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, args=["--no-sandbox"])
        page = await browser.new_page()
        await page.goto("https://fem.encar.com")

        await page.wait_for_timeout(3000)  # ждём загрузку

        cars = []

        # Пример парсинга (должно быть доработано под структуру Encar)
        items = await page.query_selector_all(".model_list li")
        for item in items[:5]:  # только первые 5
            title = await item.inner_text()
            cars.append({
                "title": title,
                "price_krw": 10000000,
                "date": "2025-07-07",
                "brand": "Kia",
                "description": "Краткое описание авто",
                "link": "https://fem.encar.com",
                "image_url": None
            })

        await browser.close()
        return cars
