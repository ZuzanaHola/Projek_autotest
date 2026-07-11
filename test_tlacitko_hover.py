from playwright.sync_api import Page, expect 

def test_kurzy_hover(page: Page):
    page.goto("https://www.engeto.cz/")

    #prejed myší na tlačítko kurzy
    image = page.locator(".area-kurzy > a:nth-child(2)")
    expect(image).to_be_visible()
    image.hover()

    #ukaze se ti menu
    title = page.locator(".area-kurzy > ul:nth-child(3) > li:nth-child(1) > ul:nth-child(2) > li:nth-child(1) > a:nth-child(1) > span:nth-child(3)")
    expect(title).to_be_visible()
    assert title.is_visible() == True

   
