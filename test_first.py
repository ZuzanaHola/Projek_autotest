
from playwright.sync_api import Page, expect

def test_kurzy_hover(page: Page):
    page.goto("https://www.engeto.cz/")

    # hover na tlacitko Kurzy
    page.locator(".area-kurzy > a").hover()

    # dropdown menu je viditelne
    expect(page.locator("#top-menu .sub-menu")).to_be_visible()

    # overeni Testing Akademie
    expect(page.get_by_text("Testing Akademie")).to_be_visible()