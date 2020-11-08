from selenium.webdriver.support.ui import Select
from model.params_for_user import Parameters
from model.users_in_groups import Users_in_groups
import re

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
        wd.find_element_by_name("submit").click()
        self.return_homepage()
        self.user_cache = None

    def edit_user(self):
        self.edit_user_by_index(0)

    def edit_user_by_index(self, index, parameters):
        wd = self.app.wd
        self.open_home_page()
        wd.find_elements_by_xpath(".//img[@alt='Edit']")[index].click()
        self.fill_in_form_user(parameters)
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.return_homepage()
        self.user_cache = None

    def edit_user_by_id(self, id, parameters):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_css_selector("a[href='edit.php?id=%s']" % id).click()
        self.fill_in_form_user(parameters)
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.return_homepage()
        self.user_cache = None

    def open_user_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        wd.find_elements_by_xpath(".//img[@alt='Edit']")[index].click()

    def open_user_view_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        wd.find_elements_by_xpath(".//img[@alt='Details']")[index].click()

    def selected_user(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def selected_user_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def selected_user_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def del_user(self):
        self.del_user_by_index(0)

    def del_user_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        self.selected_user_by_index(index)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.open_home_page()
        self.user_cache = None

    def del_user_by_id(self, id):
        wd = self.app.wd
        self.open_home_page()
        self.selected_user_by_id(id)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.open_home_page()
        self.user_cache = None

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
        self.change_field_value("phone2", parameters.phone2)
        self.change_field_value("email", parameters.email)
        self.change_field_value("email2", parameters.email2)
        self.change_field_value("email3", parameters.email3)
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
    user_cache = None

    def get_user_list(self):
        if self.user_cache is None:
            wd = self.app.wd
            self.open_home_page()
            self.user_cache = []
            for element in wd.find_elements_by_name("entry"):
                cells = element.find_elements_by_tag_name("td")
                firstname = cells[2].text
                lastname = cells[1].text
                address = cells[3].text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                all_phones = cells[5].text
                all_emails = cells[4].text
                self.user_cache.append(Parameters(firstname=firstname, lastname=lastname, address=address,
                                                  id=id, all_phones_from_home_page=all_phones,
                                                  all_emails_from_home_page=all_emails))
        return list(filter(None, self.user_cache))


    def get_user_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_user_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        home = wd.find_element_by_name("home").get_attribute("value")
        mobile = wd.find_element_by_name("mobile").get_attribute("value")
        work = wd.find_element_by_name("work").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Parameters(firstname=firstname, lastname=lastname, id=id, home=home,
                            mobile=mobile, work=work, phone2=phone2, email=email, email2=email2, email3=email3)

    def get_user_from_view_page(self, index):
        wd = self.app.wd
        self.open_user_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home = re.search("H: (.*)", text).group(1)
        mobile = re.search("M: (.*)", text).group(1)
        work = re.search("W: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)
        return Parameters(home=home, mobile=mobile, work=work, phone2=phone2)

    def add_in_group(self, user_id, group_id):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_css_selector("input[value='%s']" % user_id).click()
        wd.find_element_by_xpath("//select[@name='to_group']/option[@value='%s']" % group_id).click()
        wd.find_element_by_xpath("//input[@value='Add to']").click()
        self.open_home_page()

    def delete_from_group(self, name_group):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element_by_xpath("//select[@name='group']/option[text()='%s']" % name_group.name).click()
        if wd.find_elements_by_name("entry"):
            wd.find_elements_by_tag_name("td")
            wd.find_element_by_name("selected[]").click()
            wd.find_element_by_xpath("//input[@name='remove']").click()
            wd.switch_to_alert().accept()
        else:
            wd.find_element_by_xpath("//select[@name='group']/option[text()='[all]']").click()
            self.open_home_page()

    def user_exist_in_group(self, name_group):
        wd = self.app.wd
        self.open_group_with_users(name_group)
        user_id = wd.find_element_by_name("selected[]").get_attribute("value")
        select_group = wd.find_element_by_xpath("//select[@name='group']/option[text()='%s']" % name_group).click()
        group_id = wd.find_element_by_name("%s % name_group").get_attribute("value")
        return Users_in_groups(id=user_id, group_id=group_id)

    def open_group_with_users(self, name_group):
        wd = self.app.wd
        wd.find_element_by_xpath("//select[@name='group']/option[text()='%s']" % name_group).click()








