import re
from playwright.sync_api import Page, expect


def test_kurzy_hover(page: Page):

    page.goto("https://www.engeto.cz/")

    accept_button = page.locator("#cookiescript_accept")
    expect(accept_button).to_be_visible()
    accept_button.click()

    email_input = page.locator('input[name="newsletter-form-email"]')
    email_input.scroll_into_view_if_needed()
    expect(email_input).to_be_visible()

    # správně zadaný formát e-mailu
    email_input.fill("spravny.email@seznam.cz")
    je_validni = email_input.evaluate("el => el.validity.valid")
    assert je_validni is True

    page.screenshot(path="screenshot.png", full_page=True)
