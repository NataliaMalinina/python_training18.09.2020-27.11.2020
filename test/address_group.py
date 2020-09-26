# -*- coding: utf-8 -*-
import pytest
from model.group import Group
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_address_group(app):
    app.session.login(username="admin", password="secret")
    app.create_group(Group(name=u"Университет", header=u"Кафедра №1", footer=u"Кафедра №2"))
    app.session.logout()

def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.create_group(Group(name=u" ", header=u" ", footer=u" "))
    app.session.logout()

