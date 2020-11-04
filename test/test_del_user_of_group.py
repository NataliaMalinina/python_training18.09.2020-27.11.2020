import random


def test_del_user_of_group(app, db, check_ui):
    list_of_group = db.get_group_list()
    name_of_group = random.choice(list_of_group)
    app.user.delete_of_group(name_of_group)

