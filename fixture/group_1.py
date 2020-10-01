

class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def create(self, group):
        wd = self.app.wd
        self.open_group_page()
        # init group creation
        wd.find_element_by_name("new").click()
        self.fill_in_form_group(group)
        wd.find_element_by_name("submit").click()
        self.return_groups_page()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_group_page()
        wd.find_element_by_name("selected[]").click() # select first group
        wd.find_element_by_name("delete").click()# submit delete group
        self.return_groups_page()

    def edit_group(self, group):
        wd = self.app.wd
        self.open_group_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_name("edit").click()
        self.fill_in_form_group(group)
        wd.find_element_by_name("update").click()
        self.return_groups_page()

    def return_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def return_homepage(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def fill_in_form_group(self, group):
        wd = self.app.wd
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys("%s" % group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys("%s" % group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys("%s" % group.footer)