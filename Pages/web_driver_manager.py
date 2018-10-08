from selenium import webdriver


class WebDriverManager(object):

    __driver = None

    @classmethod
    def get_web_driver(cls, browser):
        if cls.__driver is None:
            if (browser.lower()) == "chrome":
                cls.__driver = webdriver.Chrome("D:\ChromeDriver\chromedriver.exe")
            elif (browser.lower()) == "internet explorer":
                cls.__driver = webdriver.Ie("D:\IEDriverServer_x64_3.13.0\IEDriverServer.exe")

        return cls.__driver
