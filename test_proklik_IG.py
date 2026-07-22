from playwright.sync_api import sync_playwright, Page, expect
import pytest


def test_title(page: Page):
    page.goto("https://engeto.cz/")

    page = accept_cookies(page)

    with page.expect_popup() as popup:
        button = page.locator(".ci-instagram") #NAJDE ikonku na IG
        button.click()

    expect(popup.value).to_have_url("https://www.instagram.com/engeto_academy/?hl=cs")

#odklikavaní cookies 
def accept_cookies(page: Page):
    page.click("#cookiescript_accept")
    return page