from playwright.sync_api import sync_playwright
import pytest

@pytest.fixture
def page_f():
    with sync_playwright() as context: 
        browser = context.firefox.launch(headless=False, slow_mo=1000)
        page = browser.new_page() 
        yield page
        
@pytest.fixture
def page_ch():
    with sync_playwright() as context: 
        browser = context.chromium.launch()
        page = browser.new_page()
        yield page
        
@pytest.fixture
def page_ch_vis():
    with sync_playwright() as context: 
        browser = context.chromium.launch(headless=False, slow_mo=1000) #ukazka vizualni
        page = browser.new_page()
        yield page
        page.close()

@pytest.fixture
def page_viewport():
    with sync_playwright() as context: 
        browser = context.chromium.launch(headless=False, slow_mo=1500) #ukazka vizualni
        context = browser.new_context(
            viewport={"width":360, "height":720})
        page = context.new_page()
        yield page
        

@pytest.fixture
def page_devices_mobil():
    with sync_playwright() as context: 
        webkit = context.webkit
        iphone = context.devices ["iPhone 12"]
        browser = webkit.launch(headless=False, slow_mo=2000)
        context = browser.new_context(**iphone)
        page = context.new_page()
        yield page
        page.close()