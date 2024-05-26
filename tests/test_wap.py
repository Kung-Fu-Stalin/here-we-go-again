from utils import Config
from pages import HomePage


def test_wap():
    home_page = HomePage(
        browser=Config.BROWSER, 
        width=Config.WIDTH, 
        height=Config.HEIGHT
    )
    home_page.open_page(url=Config.URL)
    home_page.close_privacy_window()
    home_page.click_on_search_button()
    home_page.search(text=Config.GAME)
    home_page.make_screenshot(path=Config.SCREENSHOTS_PATH)
