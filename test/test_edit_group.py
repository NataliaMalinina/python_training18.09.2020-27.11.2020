from model.group import Group
from random import randrange

def test_edit_group(app):
    if app.group_1.count() == 0:
        app.group_1.create(Group(name="Школа", header="Номер 2", footer="Номер 3"))
    old_groups = app.group_1.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="Грибоедова")
    group.id = old_groups[index].id
    app.group_1.edit_group_by_index(index, group)
    new_groups = app.group_1.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

# def test_edit_group(app):
#     old_groups = app.group_1.get_group_list()
#     app.group_1.edit_group(Group(footer="New footer"))
#     new_groups = app.group_1.get_group_list()
#     assert len(old_groups) == len(new_groups)