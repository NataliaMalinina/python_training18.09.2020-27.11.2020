# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest
from params_for_user import Parameters, Phones, Emails

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
    
    def test_untitled_test_case(self):
        wd = self.wd
        self.open_home_page(wd)
        self.autorization(wd, login="admin", password="secret")
        self.add_new_user_in_addressbook(wd)
        self.fill_in_form(wd,
        Parameters(firstname="Iona", middlename="Tasha Fox", lastname="Donovan",
        nickname="Wynne Stanley", title="Aut qui libero et mi", company="Rhodes Steele Co", byear="2006", ayear="2004",
        address="Numquam nisi enim ad", address2="Vero eos rem reicien", notes="Labore fugiat quibu", bday="26",
        bmonth="July", aday="5", amonth="October", new_group="[none]"),

        Phones(home="Laborum Ut delectus", mobile="Eum harum est asperi", work="Consequatur Rerum o",
        fax="+1 (153) 565-7684", phone2="+1 (886) 162-2602"),

        Emails(email="dadicef@mailinator.net", email2="xobyval@mailinator.net", email3="qogyfyl@mailinator.com", homepage="Dignissimos voluptat"))
        self.return_homepage(wd)
        self.log_out(wd)

    def log_out(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def return_homepage(self, wd):
        wd.find_element_by_link_text("home page").click()

    def fill_in_form(self, wd, Parameters, Phones, Emails):
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys("%s" % Parameters.firstname)
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys("%s" % Parameters.middlename)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys("%s" % Parameters.lastname)
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys("%s" % Parameters.nickname)
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys("%s" % Parameters.title)
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys("%s" % Parameters.company)
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys("%s" % Phones.home)
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys("%s" % Phones.mobile)
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys("%s" % Phones.work)
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys("%s" % Phones.fax)
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys("%s" % Emails.email)
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys("%s" % Emails.email2)
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys("%s" % Emails.email3)
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys("%s" % Emails.homepage)
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys("%s" % Parameters.byear)
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys("%s" % Parameters.ayear)
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys("%s" % Phones.phone2)
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys("%s" % Parameters.address)
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys("%s" % Parameters.address2)
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys("%s" % Parameters.notes)
        Select(wd.find_element_by_name("bday")).select_by_visible_text("%s" % Parameters.bday)
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text("%s" % Parameters.bmonth)
        Select(wd.find_element_by_name("aday")).select_by_visible_text("%s" % Parameters.aday)
        Select(wd.find_element_by_name("amonth")).select_by_visible_text("%s" % Parameters.amonth)
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
