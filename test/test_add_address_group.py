# -*- coding: utf-8 -*-

from model.group import Group


def test_address_group(app):
    old_groups = app.group_1.get_group_list()
    group = Group(name="Университет", header="Кафедра №1", footer="Кафедра №2")
    app.group_1.create(group)
    assert len(old_groups) + 1 == app.group_1.count()
    new_groups = app.group_1.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


# def test_add_empty_group(app):
#     old_groups = app.group_1.get_group_list()
#     group = Group(name="", header="", footer="")
#     app.group_1.create(group)
#     new_groups = app.group_1.get_group_list()
#     assert len(old_groups) + 1 == len(new_groups)
#     old_groups.append(group)
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


