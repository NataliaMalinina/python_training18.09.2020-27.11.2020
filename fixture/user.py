from selenium.webdriver.support.ui import Select

class UserHelper:

    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/index.php")) or not \
                (wd.current_url.endswith("/addressbook/")):
            wd.find_element_by_link_text("home").click()
        # wd = self.app.wd
        # wd.get("http://localhost/addressbook/")

    def add_new_user_in_addressbook(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def fill(self, Parameters):
        wd = self.app.wd
        self.add_new_user_in_addressbook()
        self.fill_in_form_user(Parameters)
 #       Select(wd.find_element_by_name("new_group")).select_by_visible_text("%s" % Parameters.new_group)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_homepage()

    def edit_user(self, Parameters):
        wd = self.app.wd
        self.open_home_page()
        self.selected_user()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_in_form_user(Parameters)
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.return_homepage()

    def selected_user(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def del_user(self):
        wd = self.app.wd
        self.open_home_page()
        self.selected_user()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.open_home_page()

    def return_homepage(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)
#            Select(wd.find_element_by_name(field_name)).select_by_value(text)

    def fill_in_form_user(self, Parameters):
        wd = self.app.wd
        self.change_field_value("firstname", Parameters.firstname)
        self.change_field_value("middlename", Parameters.middlename)
        self.change_field_value("lastname", Parameters.lastname)
        self.change_field_value("company", Parameters.company)
        self.change_field_value("home", Parameters.home)
        self.change_field_value("mobile", Parameters.mobile)
        self.change_field_value("work", Parameters.work)
        self.change_field_value("email", Parameters.email)
        self.change_field_value("byear", Parameters.byear)
        self.change_field_value("address", Parameters.address)
        self.select_by_value("bday", Parameters.bday)
        self.select_by_value("bmonth", Parameters.bmonth)

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def select_by_value(self, field_name, text):
        wd = self.app.wd
        Select(wd.find_element_by_name(field_name)).select_by_value(text)
