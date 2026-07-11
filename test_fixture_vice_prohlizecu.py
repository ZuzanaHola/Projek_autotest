from playwright.sync_api import Page, expect, sync_playwright
import pytest


def test_engeto_firefox(page_f: Page):
    page = page_f
    # přejdi na stránku Engeta
    page.goto("https://www.engeto.cz/")

    # klikneme na tlacitko accept
    accept_button = page.locator("#cookiescript_accept")
    expect(accept_button).to_be_visible() #ocekávám, že bude tlačítko videt 
    accept_button.click() #nasledne na nej kliknu accept

    # zkontrolujeme, ze se cookie bar schoval
    cookie_bar = page.locator("#cookiescript_injected")

    expect(cookie_bar).not_to_be_visible()

def test_engeto_chrom(page_ch: Page):
    page = page_ch
    # přejdi na stránku Engeta
    page.goto("https://www.engeto.cz/")

    # klikneme na tlacitko accept
    accept_button = page.locator("#cookiescript_accept")
    expect(accept_button).to_be_visible() #ocekávám, že bude tlačítko videt 
    accept_button.click() #nasledne na nej kliknu accept

    # zkontrolujeme, ze se cookie bar schoval
    cookie_bar = page.locator("#cookiescript_injected")

    expect(cookie_bar).not_to_be_visible()


def test_engeto_chrom_vizual(page_ch_vis:Page):
    page = page_ch_vis
    # přejdi na stránku Engeta
    page.goto("https://www.engeto.cz/")

    # klikneme na tlacitko accept
    accept_button = page.locator("#cookiescript_accept")
    expect(accept_button).to_be_visible() #ocekávám, že bude tlačítko videt 
    accept_button.click() #nasledne na nej kliknu accept

    # zkontrolujeme, ze se cookie bar schoval
    cookie_bar = page.locator("#cookiescript_injected")

    expect(cookie_bar).not_to_be_visible()


def test_engeto_mensi_stranka(page_viewport: Page):
        page = page_viewport
    
        # přejdi na stránku Engeta
        page.goto("https://www.engeto.cz/")

        # klikneme na tlacitko accept
        accept_button = page.locator("#cookiescript_accept")
        expect(accept_button).to_be_visible() #ocekávám, že bude tlačítko videt 
        accept_button.click() #nasledne na nej kliknu accept
    
        # zkontrolujeme, ze se cookie bar schoval
        cookie_bar = page.locator("#cookiescript_injected")
   
        expect(cookie_bar).not_to_be_visible()



def test_engeto_mobil(page_devices_mobil: Page):
        page = page_devices_mobil

        # přejdi na stránku Engeta
        page.goto("https://www.engeto.cz/")

        # klikneme na tlacitko accept
        accept_button = page.locator("#cookiescript_accept")
        expect(accept_button).to_be_visible() #ocekávám, že bude tlačítko videt 
        accept_button.click() #nasledne na nej kliknu accept
    
        # zkontrolujeme, ze se cookie bar schoval
        cookie_bar = page.locator("#cookiescript_injected")
   
        expect(cookie_bar).not_to_be_visible()