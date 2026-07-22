import re
from playwright.sync_api import Page, expect


def test_email(page: Page):

    page.goto("https://www.engeto.cz/")

    accept_button = page.locator("#cookiescript_accept")
    expect(accept_button).to_be_visible()
    accept_button.click()

    email_input = page.locator('input[name="newsletter-form-email"]')
    email_input.scroll_into_view_if_needed()
    expect(email_input).to_be_visible()

    # chybně zadaný formát e-mailu
    email_input.fill("chybny_email_bez_zavinace")

    button = page.locator("a.size-xl:nth-child(2)") 
    button.click()

   #  email_input.press("Enter")  # odešle formulář místo hledání tlačítka

    chybova_hlaska = email_input.evaluate("el => el.validationMessage")
    
    

    #breakpoint()

    assert chybova_hlaska != "", "Chybová hláška se nezobrazila"

    page.screenshot(path="screenshot.png", full_page=True)