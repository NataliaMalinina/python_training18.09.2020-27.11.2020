# -*- coding: utf-8 -*-
from model.params_for_user import Parameters


def test_add_user(app, json_users):
    user = json_users
    old_user = app.user.get_user_list()
    app.user.fill(user)
    assert len(old_user) + 1 == app.user.count()
    new_user = app.user.get_user_list()
    old_user.append(user)
    assert sorted(old_user, key=Parameters.id_or_max) == sorted(new_user, key=Parameters.id_or_max)

