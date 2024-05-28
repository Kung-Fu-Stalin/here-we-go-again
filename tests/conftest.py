import pytest

from utils import Driver
from utils import Config
from utils import get_logger


logger = get_logger(__name__)


@pytest.fixture(scope="session", autouse=True)
def close_browser():
    driver = Driver(
        browser=Config.BROWSER, 
        device=Config.DEVICE
    )
    yield
    logger.info(f"Closing {Config.BROWSER} browser window")
    driver.quit()
