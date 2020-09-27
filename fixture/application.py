from selenium import webdriver
#from selenium.webdriver.support.ui import Select
from fixture.session import SessionHelper
from fixture.group_1 import GroupHelper
from fixture.add_user import UserHelper

class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.group_1 = GroupHelper(self)
        self.add_user = UserHelper(self)
        #self.wd = Select(self)


    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")


    def destroy(self):
        self.wd.quit()
