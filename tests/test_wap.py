from utils import Config
from pages import HomePage


def test_wap():
    home_page = HomePage(
        browser=Config.BROWSER,
        device=Config.DEVICE
    )
    home_page.open_page(url=Config.URL)
    home_page.close_privacy_window()
    home_page.click_on_search_button()
    home_page.search(text=Config.GAME)
    home_page.switch_to_channels()
    home_page.scroll_search_results(count=5)
    home_page.select_random_channel()
    home_page.make_screenshot(Config.SCREENSHOTS_PATH)
