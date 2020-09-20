# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
    
    def test_untitled_test_case(self):
        wd = self.wd
        self.open_home_page(wd)
        self.autorization(wd)
        self.add_new_user_in_addressbook(wd)
        self.fill_in_form(wd)
        self.return_homepage(wd)
        self.log_out(wd)

    def log_out(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def return_homepage(self, wd):
        wd.find_element_by_link_text("home page").click()

    def fill_in_form(self, wd):
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys("Iona")
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys("Tasha Fox")
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys("Donovan")
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys("Wynne Stanley")
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys("Aut qui libero et mi")
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys("Rhodes Steele Co")
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys("Laborum Ut delectus")
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys("Eum harum est asperi")
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys("Consequatur Rerum o")
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys("+1 (153) 565-7684")
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys("dadicef@mailinator.net")
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys("xobyval@mailinator.net")
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys("qogyfyl@mailinator.com")
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys("Dignissimos voluptat")
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys("2006")
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys("2004")
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys("+1 (886) 162-2602")
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys("Numquam nisi enim ad")
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys("Vero eos rem reicien")
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys("Labore fugiat quibu")
        Select(wd.find_element_by_name("bday")).select_by_visible_text("26")
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text("July")
        Select(wd.find_element_by_name("aday")).select_by_visible_text("5")
        Select(wd.find_element_by_name("amonth")).select_by_visible_text("October")
        Select(wd.find_element_by_name("new_group")).select_by_visible_text("[none]")
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def add_new_user_in_addressbook(self, wd):
        wd.find_element_by_link_text("add new").click()

    def autorization(self, wd):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
