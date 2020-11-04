import random
from model.params_for_user import Parameters


def test_del_user_of_group(app, db, check_ui):
    list_of_group = db.get_group_list()
    name_of_group = random.choice(list_of_group)
    app.user.delete_of_group(name_of_group)
    if check_ui:
        assert sorted(list_of_group, key=Parameters.id_or_max) == sorted(app.group_1.get_group_list(),
                                                                         key=Parameters.id_or_max)


