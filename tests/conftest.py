import logging

import pytest

from utils import Config, Driver


logger = logging.getLogger(__name__)


@pytest.fixture(scope="session", autouse=True)
def close_browser():
    driver = Driver(
        browser=Config.BROWSER,
        device=Config.DEVICE
    )
    yield
    logger.info(f"Closing {Config.BROWSER} browser window")
    driver.quit()
