import pytest

from utils import Driver
from utils import Config


@pytest.fixture(scope="session", autouse=True)
def driver():
    driver = Driver(
        browser=Config.BROWSER, 
        width=Config.WIDTH, 
        height=Config.HEIGHT
    )
    yield
    driver.quit()
