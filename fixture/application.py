from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group_1 import GroupHelper
from fixture.user import UserHelper

class Application:

    def __init__(self, browser, base_url, login, password):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.wd.implicitly_wait(1)
        self.session = SessionHelper(self)
        self.group_1 = GroupHelper(self)
        self.user = UserHelper(self)
        self.base_url = base_url
        self.login = login
        self.password = password

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()
