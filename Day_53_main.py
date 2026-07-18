import asyncio
import random
from playwright.async_api import async_playwright

# --- SAMPLE SOURCE DATA ---
# This simulates rows from an Excel or CSV file
DATA_RECORDS = [
    {"name": "Arjun Nair", "email": "arjun@example.com", "department": "Engineering", "notes": "Onboarded March 2026"},
    {"name": "Sarah Jenkins", "email": "sarah.j@example.com", "department": "Marketing",
     "notes": "Remote setup complete"},
    {"name": "Kenji Sato", "email": "sato.k@example.com", "department": "Finance",
     "notes": "Requires software license key"},
]

# --- TARGET CONFIGURATIONS ---
# Replace this with your actual target company database, spreadsheet portal, or internal web form URL
TARGET_URL = "https://example.com/internal-data-entry-form"

# Target Form Input Selectors (CSS identifiers matching form fields)
NAME_FIELD = "input[name='employee_name'], #name-input"
EMAIL_FIELD = "input[name='employee_email'], #email-input"
DEPT_DROPDOWN = "select[name='department'], #dept-select"
NOTES_FIELD = "textarea[name='notes'], #notes-input"
SUBMIT_BUTTON = "button[type='submit'], #submit-btn"


async def process_data_entry():
    async with async_playwright() as p:
        print("[System] Starting data entry engine pipeline...")

        # Launching browser. headless=False allows you to see the script filling the forms live.
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        # Navigate to the target portal
        print(f"[Navigation] Opening target form: {TARGET_URL}")
        await page.goto(TARGET_URL)

        total_records = len(DATA_RECORDS)

        for index, record in enumerate(DATA_RECORDS):
            print(f"\n[Processing] Record {index + 1} of {total_records}: {record['name']}")

            try:
                # 1. Ensure the field is fully rendered and interactable on screen
                await page.wait_for_selector(NAME_FIELD, timeout=10000)

                # 2. Clear old input strings and write the fresh data
                await page.fill(NAME_FIELD, record["name"])
                await page.fill(EMAIL_FIELD, record["email"])

                # 3. Handle dropdown selections cleanly
                # Works with either the visual text option display or the underlying value string
                await page.select_option(DEPT_DROPDOWN, label=record["department"])

                # 4. Handle text area blocks
                await page.fill(NOTES_FIELD, record["notes"])

                # Human-like typing/pacing buffer (0.5 to 1.5 second pause)
                # Helps ensure data scripts do not choke fast internal database listeners
                await asyncio.sleep(random.uniform(0.5, 1.5))

                # 5. Commit the record
                print(f"[Action] Submitting form entry details...")
                await page.click(SUBMIT_BUTTON)

                # 6. Wait for a confirmation or a reload loop before cycling to the next record
                # Adjust this depending on whether your target system reloads or clears the fields
                await page.wait_for_load_state("networkidle")
                print(f"[Success] Record {index + 1} finalized successfully.")

            except Exception as error:
                print(f"[Error] Failed on record line {index + 1}: {error}")
                print("[Pause] Halting for 5 seconds to let the system stabilize before trying next record...")
                await asyncio.sleep(5.0)

        print("\n[System] All data matrix pipelines executed.")
        print("[Close] Shutting down active session environments...")
        await browser.close()


if __name__ == "__main__":
    # Run the main async script block
    asyncio.run(process_data_entry())