from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group_1 import GroupHelper
from fixture.user import UserHelper
from fixture.redact_group import GroupHelperredact
from fixture.redact_user import UserHelperredact

class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.group_1 = GroupHelper(self)
        self.user = UserHelper(self)
        self.redact_group = GroupHelperredact(self)
        self.redact_user = UserHelperredact(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")


    def destroy(self):
        self.wd.quit()
