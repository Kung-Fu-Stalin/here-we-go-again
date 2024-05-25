from utils import Config


def test_wap(driver):
    driver.get(Config.URL)
    driver.save_screenshot('screenie2.png')
