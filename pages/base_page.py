
from typing import Union
from pathlib import Path
from datetime import datetime

from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions

from utils import Driver
from utils import get_logger


logger = get_logger(__name__)


class BasePage:

    WAIT_TIME = 10
    
    def __init__(self, browser: str, width: int, height: int) -> None:
        logger.info(
            f"Create a new browser instance: {browser}. "
            f"Width: {width} Height: {height}"
        )
        self.driver = Driver(browser, width, height)
        self.driver_wait = WebDriverWait(self.driver, self.WAIT_TIME)

    def open_page(self, url: str) -> None:
        logger.info(f"Open page: {url}")
        self.driver.get(url)

    def make_screenshot(self, path: Union[Path, str]) -> Path:
        if isinstance(path, str):
            path = Path(path)
        path.mkdir(parents=True, exist_ok=True)
        date_stamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        filename = f"screenshot-{date_stamp}.png"
        logger.info(f"Taking screenshot: {filename}")
        screenshot_path = Path(path, filename)
        self.driver.save_screenshot(screenshot_path)
        logger.info(f"Screenshot is available here: {screenshot_path}")
        return screenshot_path
    
    def find_element(self, *location):
        logger.info(f"Finding element with location: {location}")
        try:
            element = self.driver_wait.until(
                expected_conditions.visibility_of_element_located(
                    location
                )
            )
            logger.info(f"Element found: {location}")
            return element
        except TimeoutException:
            logger.error(f"Element not found: {location}")
            return None

    def click_element(self, *location) -> None:
        try:
            element = self.find_element(*location)
            if element:
                element.click()
        except TimeoutException:
            logger.error(f"Could not click the element: {location}")

    def enter_text(self, *location, text: str) -> None:
        try:
            element = self.find_element(*location)
            if element:
                element.send_keys(text)
        except TimeoutException:
            logger.error(f"Could not enter text in the element: {location}")
    