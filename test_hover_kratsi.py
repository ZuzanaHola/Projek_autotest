from playwright.sync_api import Page, expect 

def test_kurzy_hover(page: Page):
    page.goto("https://www.engeto.cz/")
    
    accept_button = page.locator("#cookiescript_accept")
    expect(accept_button).to_be_visible() #ocekávám, že bude tlačítko videt 
    accept_button.click() #nasledne na nej kliknu accept

    # hover na tlacitko Kurzy
    page.locator(".area-kurzy > a").hover()

    # dropdown menu je viditelne
    expect(page.locator("#top-menu .area-kurzy .sub-menu")).to_be_visible()

    # overeni Testing Akademie
    expect(page.locator("#top-menu .area-kurzy .sub-menu").get_by_text("Testing Akademie")).to_be_visible()

    page.screenshot(path="screenshot.png", full_page=True)
