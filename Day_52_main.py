import asyncio
from playwright.async_api import async_playwright

# --- CONFIGURATION ---
TARGET_ACCOUNT = "nasa"  # Replace with any public Instagram handle
TARGET_URL = f"https://www.instagram.com/{TARGET_ACCOUNT}/"


async def monitor_profile_metrics():
    async with async_playwright() as p:
        print(f"[System] Initializing anonymous monitor instance...")

        # Launching a normal browser instance with custom arguments to bypass basic blocks
        browser = await p.chromium.launch(
            headless=False,
            args=["--disable-blink-features=AutomationControlled"]
        )

        # Creating a realistic browser signature context
        context = await browser.new_context(
            viewport={'width': 1280, 'height': 800},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
        )

        page = await context.new_page()

        try:
            print(f"[Navigation] Loading profile view for: @{TARGET_ACCOUNT}")
            await page.goto(TARGET_URL, wait_until="domcontentloaded")

            # Wait for the profile bio or metric header elements to parse into the DOM
            # Instagram often structures headers containing strings like "followers" or "following"
            metric_selector = "header ul li"
            await page.wait_for_selector(metric_selector, timeout=15000)

            # Grab all listing elements inside the header profile stats row
            stat_elements = await page.query_selector_all(metric_selector)

            print(f"\n=== Current Public Stats for @{TARGET_ACCOUNT} ===")
            for index, element in enumerate(stat_elements):
                text_content = await element.inner_text()
                # Cleans up multi-line layout formatting strings
                clean_text = text_content.replace("\n", " ")
                print(f"- {clean_text}")
            print("=" * 40 + "\n")

        except Exception as error:
            print(f"[Error] Failed to read public metric elements: {error}")
            print("[Tip] Instagram may be displaying a mandatory login redirect wall for this session.")

        finally:
            print("[System] Closing tracker environment instance.")
            await browser.close()


if __name__ == "__main__":
    asyncio.run(monitor_profile_metrics())