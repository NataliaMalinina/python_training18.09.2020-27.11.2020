# -*- coding: utf-8 -*-
from model.group import Group


def test_address_group(app):
    app.session.login(username="admin", password="secret")
    app.group_1.create(Group(name=u"Университет", header=u"Кафедра №1", footer=u"Кафедра №2"))
    app.session.logout()

def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group_1.create(Group(name=u" ", header=u" ", footer=u" "))
    app.session.logout()

