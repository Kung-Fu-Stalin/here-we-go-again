import time 

from selenium import webdriver

from utils import Config


class Driver:

    _driver = None

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Driver, cls).__new__(cls)
            cls._driver = cls.get_driver(cls)
        return cls._driver

    def get_driver(self):
        if Config.BROWSER == "chrome":
            mobile_params = {
                "deviceMetrics": {
                    "width": Config.WIDTH,
                    "height": Config.HEIGHT
                }
            }
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_experimental_option("mobileEmulation", mobile_params)
            driver = webdriver.Chrome(options=chrome_options)
        elif Config.BROWSER == "firefox":
            firefox_options = webdriver.FirefoxOptions()
            driver = webdriver.Firefox(options=firefox_options)
            driver.set_window_size(Config.WIDTH, Config.HEIGHT)
        return driver
    

if __name__ == '__main__':
    s1 = Driver()
    s1.get(Config.URL)
    time.sleep(10)

    s1.quit()
    