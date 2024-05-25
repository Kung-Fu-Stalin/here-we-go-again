import pytest

from utils import Driver


@pytest.fixture(scope="session")
def driver():
    driver = Driver()
    yield driver
    driver.quit()
