from playwright.sync_api import Page, expect, sync_playwright


def test_engeto_firefox():

    #vytvoreni page pomoci withblock firefox
    with sync_playwright() as context: 
        browser = context.firefox.launch()
        page = browser.new_page()
        
        # přejdi na stránku Engeta
        page.goto("https://www.engeto.cz/")

        # klikneme na tlacitko accept
        accept_button = page.locator("#cookiescript_accept")
        expect(accept_button).to_be_visible() #ocekávám, že bude tlačítko videt 
        accept_button.click() #nasledne na nej kliknu accept
    
        # zkontrolujeme, ze se cookie bar schoval
        cookie_bar = page.locator("#cookiescript_injected")
   
        expect(cookie_bar).not_to_be_visible()

def test_engeto_chrom():

    #vytvoreni page pomoci withblock firefox
    with sync_playwright() as context: 
        browser = context.chromium.launch()
        page = browser.new_page()
        
        # přejdi na stránku Engeta
        page.goto("https://www.engeto.cz/")

        # klikneme na tlacitko accept
        accept_button = page.locator("#cookiescript_accept")
        expect(accept_button).to_be_visible() #ocekávám, že bude tlačítko videt 
        accept_button.click() #nasledne na nej kliknu accept
    
        # zkontrolujeme, ze se cookie bar schoval
        cookie_bar = page.locator("#cookiescript_injected")
   
        expect(cookie_bar).not_to_be_visible()


def test_engeto_chrom_vizual():

    #vytvoreni page pomoci withblock firefox
    with sync_playwright() as context: 
        browser = context.chromium.launch(headless=False, slow_mo=2000) #ukazka vizualni
        page = browser.new_page()
        
        # přejdi na stránku Engeta
        page.goto("https://www.engeto.cz/")

        # klikneme na tlacitko accept
        accept_button = page.locator("#cookiescript_accept")
        expect(accept_button).to_be_visible() #ocekávám, že bude tlačítko videt 
        accept_button.click() #nasledne na nej kliknu accept
    
        # zkontrolujeme, ze se cookie bar schoval
        cookie_bar = page.locator("#cookiescript_injected")
   
        expect(cookie_bar).not_to_be_visible()


