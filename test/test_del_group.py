from model.group import Group
from random import randrange


def test_some_group(app):
    if app.group_1.count() == 0:
        app.group_1.create(Group(name= "тест"))
    old_groups = app.group_1.get_group_list()
    index = randrange(len(old_groups))
    app.group_1.delete_group_by_index(index)
    new_groups = app.group_1.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups[index:index+1] = []
    assert old_groups == new_groups
