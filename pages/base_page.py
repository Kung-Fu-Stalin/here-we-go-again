import time
from typing import Union
from pathlib import Path
from datetime import datetime

from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin

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
        self.action_chains = ActionChains(self.driver)
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

    def find_web_element(self, location: tuple[str, str]) -> WebElement:
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

    def click_on_element(self, location: tuple[str, str]) -> WebElement:
        try:
            element = self.driver_wait.until(
                expected_conditions.visibility_of_element_located(
                    location
                )
            )
            if element:
                element.click()
                return element
        except TimeoutException:
            logger.error(f"Could not click the element: {location}")

    def enter_text(self, location: tuple[str, str], text: str) -> WebElement:
        try:
            element = self.driver_wait.until(
                expected_conditions.visibility_of_element_located(
                    location
                )
            )
            if element:
                element.send_keys(text)
                return element
        except TimeoutException:
            logger.error(f"Could not enter text in the element: {location}")

    def scroll_from_element(self,
                            location: tuple[str, str],
                            delta_x: int,
                            delta_y: int):
        element = self.find_web_element(location)
        scroll_origin = ScrollOrigin.from_element(element)
        self.action_chains.scroll_from_origin(
            scroll_origin, delta_x, delta_y
        ).perform()

    def wait_until_video_start(self):
        js_script = """
            const video = document.querySelector('video');
            if (video) {
                return video.currentTime && !video.paused && !video.ended
            }
            return false;
            """
        attempts = 5
        while attempts > 0:
            logger.info(f"Checking stream status. Attempt left: {attempts}")
            if self.driver.execute_script(js_script):
                logger.info("Stream started.")
                break
            attempts -= 1
            time.sleep(3)
            return
        logger.error("Stream is not started after 5 attempts")

    @staticmethod
    def send_keys_on_element(element: WebElement, key: str) -> None:
        element.send_keys(key)
