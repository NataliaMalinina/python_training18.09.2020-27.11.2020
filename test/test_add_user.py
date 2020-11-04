# -*- coding: utf-8 -*-
from model.params_for_user import Parameters



def test_add_user(app, db, json_users, check_ui):
    user = json_users
    old_user = db.get_user_list()
    app.user.fill(user)
    new_user = db.get_user_list()
    old_user.append(user)
    assert sorted(old_user, key=Parameters.id_or_max) == sorted(new_user, key=Parameters.id_or_max)
    if check_ui:
        assert sorted(new_user, key=Parameters.id_or_max) == sorted(app.user.get_user_list(),
                                                                         key=Parameters.id_or_max)
