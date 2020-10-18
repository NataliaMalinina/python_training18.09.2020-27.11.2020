# -*- coding: utf-8 -*-
from model.params_for_user import Parameters
import pytest
import random
import string


def random_user(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_user_digits(prefix, maxlen):
    symbols = string.digits + string.punctuation + " "*6
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [
    Parameters(firstname=random_user("firstname", 10), middlename=random_user("middlename", 10),
    lastname=random_user("lastname", 20), company=random_user("company", 25), address=random_user("address", 31),
        home=random_user_digits("home", 13), mobile=random_user_digits("mobile", 12), work=random_user_digits("work", 15),
            phone2=random_user_digits("phone2", 20), email=random_user("email", 34))
    for i in range(2)
]


@pytest.mark.parametrize("user", testdata, ids=[repr(x) for x in testdata])
def test_add_user(app, user):
    old_user = app.user.get_user_list()
    app.user.fill(user)
    assert len(old_user) + 1 == app.user.count()
    new_user = app.user.get_user_list()
    old_user.append(user)
    assert sorted(old_user, key=Parameters.id_or_max) == sorted(new_user, key=Parameters.id_or_max)

