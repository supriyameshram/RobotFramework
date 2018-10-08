from Pages.web_driver_wait import Web

class LoginPage(object):

    __url = "http://thetestingworld.com"

    def open(self):
        self._web.open(self.__url)

    def __init__(self, browser):
        self._web = Web(browser)

    def click_login_link(self, city):
        self._web.get_web_element_by_xpath("//select[@name='fromPort']/option[@value='{}']".format(city)).click()

    def select_destination_city(self, city):
        self._web.get_web_element_by_xpath("//select[@name='toPort']/option[@value='{}']".format(city)).click()

    def search_for_flights(self):
        self._web.get_web_element_by_xpath("//input[@type='submit']").click()

    def get_found_flights(self):
        return self._web.get_web_elements_by_xpath("//table[@class='table']/tbody/tr")

    def close(self):
        self._web.close_all()