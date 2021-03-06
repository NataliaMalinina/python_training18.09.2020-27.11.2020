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

    def get_user_list(self, order='asc'):
        cursor = self.connection.cursor()
        list = []
        try:
            cursor.execute(f"select id, firstname, middlename, lastname, address, home, mobile, work, phone2, "
                           f"email, email2, email3 "
                           f"from addressbook where deprecated='0000-00-00 00:00:00' order by id {order}")
            for row in cursor:
                (id, firstname, middlename, lastname, address, home, mobile, work, phone2, email,
                                                                                    email2, email3) = row
                list.append(Parameters(id=str(id), firstname=firstname, middlename=middlename,
                                        lastname=lastname, address=address, home=home, mobile=mobile, work=work,
                                       phone2=phone2, email=email, email2=email2, email3=email3))
        finally:
            cursor.close()
        return list

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

    def get_groups_for_user(self, id):
        cursor = self.connection.cursor()
        list = []
        try:
            cursor.execute(f"select group_id from address_in_groups where deprecated='0000-00-00 00:00:00' "
                           f"and id = {id}")
            for row in cursor:
                group_id = row
                list.append(*group_id)
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()


    # def get_user_by_id(self, id):
    #     cursor = self.connection.cursor()
    #     try:
    #         cursor.execute(f"select id, firstname, lastname, address, home, mobile, work, phone2, email,"
    #                        f"email2, email3 from addressbook where deprecated='0000-00-00 00:00:00' "
    #                        f"and id = {id} limit 1")
    #         for row in cursor:
    #             (id, firstname, lastname, address, home, mobile, work, phone2, email, email2, email3) = row
    #             user = Parameters(id=str(id), firstname=firstname, lastname=lastname,
    #                                        address=address, home=home, mobile=mobile, work=work, phone2=phone2,
    #                                        email=email, email2=email2, email3=email3)
    #     finally:
    #         cursor.close()
    #         return user

    def destroy(self):
        self.connection.close()


