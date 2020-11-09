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
    founded = False
    all_groups = [int(group.id) for group in list_of_group]
    for user in list_of_users:
        groups = db.get_groups_for_user(user.id)
        exc_groups = list(set(all_groups) - set(groups))
        if len(exc_groups) > 0:
            test_user_id = user.id
            test_user_add_group = exc_groups[0]
            app.user.add_in_group(test_user_id, test_user_add_group)
            founded = True
            break
    if not founded:
        app.user.fill(Parameters(firstname="NNNNNN", bday="0", bmonth="-"))
        list_of_users = db.get_user_list(order='desc')
        for user in list_of_users:
            groups = db.get_groups_for_user(user.id)
            exc_groups = list(set(all_groups) - set(groups))
            if len(exc_groups) > 0:
                test_user_id = user.id
                test_user_add_group = exc_groups[0]
                app.user.add_in_group(test_user_id, test_user_add_group)
                break
    assert test_user_add_group in db.get_groups_for_user(test_user_id)
    if check_ui:
        assert sorted(list_of_users, key=Parameters.id_or_max) == sorted(app.user.get_user_list(), key=Parameters.id_or_max)
        assert sorted(list_of_group, key=Parameters.id_or_max) == sorted(app.group_1.get_group_list(), key=Parameters.id_or_max)

