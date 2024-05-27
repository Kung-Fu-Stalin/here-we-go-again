import random
import time

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
    SEARCH_RESULTS = \
        By.XPATH, '//*[@id="__next"]/div/main/div/div/section[1]/div[2]/a/div'
    CHANNELS = \
        By.XPATH, "//*[@id='__next']/div/nav/div/div[2]/div/ul/li[2]/a/div/div/p"
    LIST_RESULTS = \
        By.CSS_SELECTOR, ".gbzdtz > div:nth-child(1)"
    FIRST_RESULT = \
        By.XPATH, '//*[@id="__next"]/div/main/div/div'

    def close_privacy_window(self) -> None:
        logger.info("Click on close button on privacy policy window")
        self.click_on_element(self.PRIVACY_WINDOW_CLOSE_BUTTON)
    
    def click_on_search_button(self)-> None:
        logger.info("Click on search button")
        self.click_on_element(self.SEARCH_BUTTON)

    def search(self, text: str)-> None:
        logger.info(f"Enter: {text} into search field")
        element = self.enter_text(self.SEARCH_INPUT, text)
        self.send_keys_on_element(element=element, key=Keys.ENTER)
        self.find_web_element(self.SEARCH_RESULTS)

    def switch_to_channels(self):
        self.click_on_element(self.CHANNELS)

    def scroll_search_results(self, count: int):
        for _ in range(count):
            self.scroll_from_element(self.FIRST_RESULT, delta_x=0, delta_y=200)
            time.sleep(1)

    def select_random_channel(self):
        channels = self.driver.execute_script(f"return document.querySelector(\"[role='list']\").childNodes;")
        selectable_channels = [channel for channel in channels if channel.is_displayed()]
        channel = random.choice(selectable_channels)
        channel.click()
        self.wait_until_video_start()
