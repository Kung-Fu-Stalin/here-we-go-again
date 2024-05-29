from selenium import webdriver


class Driver:

    android_headers_template = {
        "User-Agent":
            "Mozilla/5.0 (Linux; Android 14; {device}) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/89.0.4389.72 Mobile Safari/537.36",
        "Device-Model": "{device}",
        "Device-OS": "Android 14",
        "App-Version": "1.0.0"
    }

    iphone_headers_template = {
        "User-Agent":
            "Mozilla/5.0 (iPhone; CPU iPhone OS 16 like Mac OS X) "
            "AppleWebKit/605.1.15 (KHTML, like Gecko) "
            "Version/14.0 Mobile/15E148 Safari/604.1",
        "Device-Model": "{device}",
        "Device-OS": "iOS 16",
        "App-Version": "1.0.0"
    }
    _instances = {}

    def __new__(cls, browser: str, device):
        key = (browser, device.name)
        if key not in cls._instances:
            instance = super(Driver, cls).__new__(cls)
            instance._driver = cls.get_driver(browser, device)
            cls._instances[key] = instance._driver
        return cls._instances[key]

    @classmethod
    def generate_user_agent(cls, device):
        if "iphone" in device.name.lower():
            headers = cls.iphone_headers_template
        else:
            headers = cls.android_headers_template
        return {
            key: value.format(device=device.name)
            for key, value in headers.items()
        }

    @classmethod
    def get_driver(cls, browser: str, device):
        user_agent = cls.generate_user_agent(device)
        if browser == "chrome":
            chrome_options = webdriver.ChromeOptions()
            # Problem on Ubuntu 24.04. Scroll with enabled mobile emulation doesn't work.
            # Related StackOverflow thread:
            # https://stackoverflow.com/questions/22722727/chrome-devtools-mobile-emulation-scroll-not-working
            # chrome_options.add_experimental_option("mobileEmulation", mobile_params)
            chrome_options.add_argument(f'--user-agent={user_agent}')
            chrome_options.add_argument(
                f"--window-size={device.width},{device.height}"
            )
            driver = webdriver.Chrome(options=chrome_options)
        elif browser == "firefox":
            firefox_options = webdriver.FirefoxOptions()
            firefox_options.set_preference(
                "general.useragent.override",
                user_agent["User-Agent"]
            )
            driver = webdriver.Firefox(options=firefox_options)
            driver.set_window_size(int(device.width), int(device.height))
        return driver
