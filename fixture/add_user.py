from selenium.webdriver.support.ui import Select

class UserHelper:

    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        wd.get("http://localhost/addressbook/")

    def add_new_user_in_addressbook(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def fill_in_form(self, Parameters):
        wd = self.app.wd
        self.add_new_user_in_addressbook()
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
        self.return_homepage()

    def edit_user(self):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys("Bruno")
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys("Wyoming Harrison")
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys("Koch")
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys("Green and Petty LLC")
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys("Nobis molestiae dolo")
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys("+1 (255) 254-8172")
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys("+1 (255) 254-8000")
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys("cidilaqyf@mailinator.com")
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys("2000")
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys("Quia laboris dolorem")
        Select(wd.find_element_by_name("bday")).select_by_visible_text("7")
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text("May")
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.return_homepage()

    def return_homepage(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()