# -*- coding: utf-8 -*-
import pytest
from application import Application
from application import Parameters

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_user(app):
    app.login(username="admin", password="secret")
    app.fill_in_form(Parameters(firstname="Iona", middlename="Tasha Fox", lastname="Donovan",
        company="Rhodes Steele Co", address="Numquam nisi enim ad", home="Laborum Ut delectus",
        mobile="Eum harum est asperi", work="Consequatur Rerum o", email="dadicef@mailinator.net",
        byear="2006", bday="26", bmonth="July", new_group="[none]"))
    app.log_out_user()


