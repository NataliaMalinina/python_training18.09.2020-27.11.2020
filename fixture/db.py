import pymysql.cursors
from model.group import Group
from model.params_for_user import Parameters
from model.users_in_groups import Users_in_groups

class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        cursor = self.connection.cursor()
        list = []
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_user_list(self):
        cursor = self.connection.cursor()
        list = []
        try:
            cursor.execute("select id, firstname, middlename, lastname, address, home, mobile, email "
                           "from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, middlename, lastname, address, home, mobile, email) = row
                list.append(Parameters(id=str(id), firstname=firstname, middlename=middlename,
                                        lastname=lastname, address=address, home=home, mobile=mobile, email=email))
        finally:
            cursor.close()
        return list

    def get_user_list_for_sr(self):
        cursor = self.connection.cursor()
        r = []
        try:
            cursor.execute("select id, firstname, lastname, address, home, mobile, work, phone2, email "
                           "from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname, address, home, mobile, work, phone2, email) = row
                list.append(Parameters(id=str(id), firstname=firstname, lastname=lastname,
                                       address=address, home=home, mobile=mobile, work=work, phone2=phone2,
                                       email=email))
        finally:
            cursor.close()
        return list(filter(None, r))

    def get_users_in_groups(self):
        cursor = self.connection.cursor()
        list = []
        try:
            cursor.execute("select id, group_id from address_in_groups where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, group_id) = row
                list.append(Users_in_groups(id=str(id), group_id=str(group_id)))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()

