from selenium.webdriver.common.by import By


from pages import BasePage
from utils import get_logger


logger = get_logger(__name__)


class HomePage(BasePage):

    PRIVACY_WINDOW_CLOSE_BUTTON = \
        By.CLASS_NAME, "ScCoreButton-sc-ocjdkq-0 ScCoreButtonPrimary-sc-ocjdkq-1 lnaTdO eQdnrM"
    
    def close_privacy_window(self):
        logger.info("Click on close button on privacy policy window")
        self.click_element(self.PRIVACY_WINDOW_CLOSE_BUTTON)
