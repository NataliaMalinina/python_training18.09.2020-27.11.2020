import random
from model.params_for_user import Parameters
from model.group import Group


def test_del_user_of_group(app, db, check_ui):
    if len(db.get_user_list()) == 0:
        app.user.fill(Parameters(firstname="тест", lastname="Bbshko", address="gfgfhv jfjd12", bday="0", bmonth="-"))
    if len(db.get_group_list()) == 0:
        app.group_1.create(Group(name="тест"))
    list_of_users = db.get_user_list()
    list_of_group = db.get_group_list()
    founded = False
    all_groups = [int(group.id) for group in list_of_group]
    for user in list_of_users:
        groups = db.get_groups_for_user(user.id)
        if len(groups) > 0:
            test_user_id = user.id
            app.user.delete_from_group(random.choice(groups))
            founded = True
            break
    if not founded:
        app.user.add_in_group(random.choice(list_of_users).id, random.choice(all_groups))
        for user in list_of_users:
            groups = db.get_groups_for_user(user.id)
            if len(groups) > 0:
                test_user_id = user.id
                app.user.delete_from_group(random.choice(groups))
                break
    assert test_user_id not in db.get_groups_for_user(test_user_id)
    if check_ui:
        assert sorted(list_of_group, key=Parameters.id_or_max) == sorted(app.group_1.get_group_list(),
                                                                         key=Parameters.id_or_max)


