from selenium.webdriver.support.ui import Select
from model.params_for_user import Parameters

class UserHelper:

    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/index.php")) or not \
                (wd.current_url.endswith("/addressbook/")):
            wd.find_element_by_link_text("home").click()


    def add_new_user_in_addressbook(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def fill(self, parameters):
        wd = self.app.wd
        self.add_new_user_in_addressbook()
        self.fill_in_form_user(parameters)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_homepage()

    def edit_user(self, parameters):
        wd = self.app.wd
        self.open_home_page()
        self.selected_user()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_in_form_user(parameters)
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


    def fill_in_form_user(self, parameters):
        wd = self.app.wd
        self.change_field_value("firstname", parameters.firstname)
        self.change_field_value("middlename", parameters.middlename)
        self.change_field_value("lastname", parameters.lastname)
        self.change_field_value("company", parameters.company)
        self.change_field_value("home", parameters.home)
        self.change_field_value("mobile", parameters.mobile)
        self.change_field_value("work", parameters.work)
        self.change_field_value("email", parameters.email)
        self.change_field_value("byear", parameters.byear)
        self.change_field_value("address", parameters.address)
        self.select_by_value("bday", parameters.bday)
        self.select_by_value("bmonth", parameters.bmonth)

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def select_by_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            Select(wd.find_element_by_name(field_name)).select_by_value(text)

    def get_user_list(self):
        wd = self.app.wd
        self.open_home_page()
        users = []
        for element in wd.find_elements_by_name("entry"):
            text = element.text
            id = element.find_element_by_name("selected[]").get_attribute("value")
            users.append(Parameters(firstname=text, middlename=text, id=id))
        return users
