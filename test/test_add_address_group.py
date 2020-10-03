# -*- coding: utf-8 -*-
from model.group import Group


def test_address_group(app):
    app.group_1.create(Group(name="Университет", header="Кафедра №1", footer="Кафедра №2"))


def test_add_empty_group(app):
#app.session.login(username="admin", password="secret")
      app.group_1.create(Group(name=" ", header=" ", footer=" "))
#     app.session.logout()

