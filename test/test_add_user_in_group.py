from model.params_for_user import Parameters
import random


def test_add_user_in_group(app, db, check_ui):
    if len(db.get_user_list()) == 0:
        app.user.fill(Parameters(firstname="тест", bday="0", bmonth="-"))
    list_of_users = db.get_user_list()
    user = random.choice(list_of_users)
    list_of_group = db.get_group_list()
    name_of_group = random.choice(list_of_group)
    app.user.add_in_group(user.id, name_of_group)
    if check_ui:
        assert sorted(list_of_users, key=Parameters.id_or_max) == sorted(app.user.get_user_list(), key=Parameters.id_or_max)
        assert sorted(list_of_group, key=Parameters.id_or_max) == sorted(app.group_1.get_group_list(), key=Parameters.id_or_max)
