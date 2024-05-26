from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


from pages import BasePage
from utils import get_logger


logger = get_logger(__name__)


class HomePage(BasePage):

    PRIVACY_WINDOW_CLOSE_BUTTON = \
        By.CSS_SELECTOR, ".ScCoreButtonPrimary-sc-ocjdkq-1"
    SEARCH_BUTTON = \
        By.CSS_SELECTOR, ".hSqeuh > a:nth-child(1)"
    SEARCH_INPUT = \
        By.CSS_SELECTOR, ".ScInputBase-sc-vu7u7d-0"
    
    def close_privacy_window(self) -> None:
        logger.info("Click on close button on privacy policy window")
        self.click_element(self.PRIVACY_WINDOW_CLOSE_BUTTON)
    
    def click_on_search_button(self)-> None:
        logger.info("Click on search button")
        self.click_element(self.SEARCH_BUTTON)

    def search(self, text: str)-> None:
        logger.info(f"Enter: {text} into search field")
        element = self.enter_text(self.SEARCH_INPUT, text)
        self.send_key_on_element(element=element, key=Keys.ENTER)
        #TODO:  Add wait search results. Pulling???
