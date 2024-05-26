from selenium import webdriver


class Driver:
    
    _instances = {}

    def __new__(cls, browser: str, width: int, height: int):
        key = (browser, width, height)
        if key not in cls._instances:   
            instance = super(Driver, cls).__new__(cls)
            instance._driver = cls.get_driver(browser, width, height)
            cls._instances[key] = instance._driver
        return cls._instances[key]
    
    @staticmethod
    def get_driver(browser: str, width: int, height: int):
        if browser == "chrome":
            mobile_params = {
                "deviceMetrics": {
                    "width": int(width),
                    "height": int(height)
                }
            }
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_experimental_option("mobileEmulation", mobile_params)
            driver = webdriver.Chrome(options=chrome_options)
        elif browser == "firefox":
            firefox_options = webdriver.FirefoxOptions()
            driver = webdriver.Firefox(options=firefox_options)
            driver.set_window_size(int(width), int(height))
        return driver
