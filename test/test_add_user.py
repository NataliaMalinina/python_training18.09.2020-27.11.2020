# -*- coding: utf-8 -*-
from model.params_for_user import Parameters
import pytest
from data.add_user import testdata


@pytest.mark.parametrize("user", testdata, ids=[repr(x) for x in testdata])
def test_add_user(app, user):
    old_user = app.user.get_user_list()
    app.user.fill(user)
    assert len(old_user) + 1 == app.user.count()
    new_user = app.user.get_user_list()
    old_user.append(user)
    assert sorted(old_user, key=Parameters.id_or_max) == sorted(new_user, key=Parameters.id_or_max)

