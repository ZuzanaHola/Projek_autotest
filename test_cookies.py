from playwright.sync_api import Page, expect
import pytest 

def test_engeto(page: Page):

    # přejdi na stránku Engeta
    page.goto("https://www.engeto.cz/")

    # klikneme na tlacitko accept
    accept_button = page.locator("#cookiescript_accept")
    expect(accept_button).to_be_visible() #ocekávám, že bude tlačítko videt 
    accept_button.click() #nasledne na nej kliknu accept
    
    # zkontrolujeme, ze se cookie bar schoval
    cookie_bar = page.locator("#cookiescript_injected")
   
    expect(cookie_bar).not_to_be_visible()

