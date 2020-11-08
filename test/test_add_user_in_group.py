from model.params_for_user import Parameters
from model.group import Group
import random


def test_add_user_in_group(app, db, check_ui):
    if len(db.get_user_list()) == 0:
        app.user.fill(Parameters(firstname="тест", bday="0", bmonth="-"))
    if len(db.get_group_list()) == 0:
        app.group_1.create(Group(name="тест"))
    list_of_users = db.get_user_list()
    list_of_group = db.get_group_list()
    user_id = list_of_users[0].id
    group_id = list_of_group[0].id

    if user_id in db.get_users_in_groups():
        user_id = list_of_users[0].id + 1
        group_id = list_of_group[0].id + 1
        app.user.add_in_group(user_id, group_id)

    if user_id not in db.get_users_in_groups():



    app.user.add_in_group(user_id, group_id)


    if check_ui:
        assert sorted(list_of_users, key=Parameters.id_or_max) == sorted(app.user.get_user_list(), key=Parameters.id_or_max)
        assert sorted(list_of_group, key=Parameters.id_or_max) == sorted(app.group_1.get_group_list(), key=Parameters.id_or_max)

