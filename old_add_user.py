# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest
from model.params_for_user import Parameters

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_untitled_test_case(self):
        wd = self.wd
        self.open_home_page(wd)
        self.autorization(wd, login="admin", password="secret")
        self.add_new_user_in_addressbook(wd)
        self.fill_in_form(wd, Parameters(firstname="Iona", middlename="Tasha Fox", lastname="Donovan",
        company="Rhodes Steele Co", address="Numquam nisi enim ad", home="Laborum Ut delectus",
        mobile="Eum harum est asperi", work="Consequatur Rerum o", email="dadicef@mailinator.net",
        byear="2006", bday="26", bmonth="July", new_group="[none]"))
        self.return_homepage(wd)
        self.log_out(wd)

    def log_out(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def return_homepage(self, wd):
        wd.find_element_by_link_text("home page").click()

    def fill_in_form(self, wd, Parameters):
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys("%s" % Parameters.firstname)
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys("%s" % Parameters.middlename)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys("%s" % Parameters.lastname)
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys("%s" % Parameters.company)
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys("%s" % Parameters.home)
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys("%s" % Parameters.mobile)
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys("%s" % Parameters.work)
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys("%s" % Parameters.email)
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys("%s" % Parameters.byear)
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys("%s" % Parameters.address)
        Select(wd.find_element_by_name("bday")).select_by_visible_text("%s" % Parameters.bday)
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text("%s" % Parameters.bmonth)
        Select(wd.find_element_by_name("new_group")).select_by_visible_text("%s" % Parameters.new_group)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def add_new_user_in_addressbook(self, wd):
        wd.find_element_by_link_text("add new").click()

    def autorization(self, wd, login, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("%s" % login)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("%s" % password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()

# заполнение формы юзера

 # def fill_in_form_user(self, Parameters):
    #     wd = self.app.wd
    #     wd.find_element_by_name("firstname").clear()
    #     wd.find_element_by_name("firstname").send_keys("%s" % Parameters.firstname)
    #     wd.find_element_by_name("middlename").clear()
    #     wd.find_element_by_name("middlename").send_keys("%s" % Parameters.middlename)
    #     wd.find_element_by_name("lastname").clear()
    #     wd.find_element_by_name("lastname").send_keys("%s" % Parameters.lastname)
    #     wd.find_element_by_name("company").clear()
    #     wd.find_element_by_name("company").send_keys("%s" % Parameters.company)
    #     wd.find_element_by_name("home").clear()
    #     wd.find_element_by_name("home").send_keys("%s" % Parameters.home)
    #     wd.find_element_by_name("mobile").clear()
    #     wd.find_element_by_name("mobile").send_keys("%s" % Parameters.mobile)
    #     wd.find_element_by_name("work").clear()
    #     wd.find_element_by_name("work").send_keys("%s" % Parameters.work)
    #     wd.find_element_by_name("email").clear()
    #     wd.find_element_by_name("email").send_keys("%s" % Parameters.email)
    #     wd.find_element_by_name("byear").clear()
    #     wd.find_element_by_name("byear").send_keys("%s" % Parameters.byear)
    #     wd.find_element_by_name("address").clear()
    #     wd.find_element_by_name("address").send_keys("%s" % Parameters.address)
    #     Select(wd.find_element_by_name("bday")).select_by_visible_text("%s" % Parameters.bday)
    #     Select(wd.find_element_by_name("bmonth")).select_by_visible_text("%s" % Parameters.bmonth)
