# -*- coding: utf-8 -*-

from model.params_for_user import Parameters


def test_add_user(app):
    old_user = app.user.get_user_list()
    user = Parameters(firstname="Iona", lastname="Donovan") #middlename="Tasha Fox", lastname="Donovan",
                              # company="Rhodes Steele Co", address="Numquam nisi enim ad", home="Laborum Ut delectus",
                              # mobile="Eum harum est asperi", work="Consequatur Rerum o", email="dadicef@mailinator.net",
                              # byear="2006", bday="26", bmonth="July", new_group="[none]")
    app.user.fill(user)
    new_user = app.user.get_user_list()
    assert len(old_user) + 1 == app.user.count()
    old_user.append(user)
    assert sorted(old_user, key=Parameters.id_or_max) == sorted(new_user, key=Parameters.id_or_max)




