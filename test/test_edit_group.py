from model.group import Group


def test_edit_group(app):
    old_groups = app.group_1.get_group_list()
    group = Group(name="Грибоедова")
    group.id = old_groups[0].id
    if app.group_1.count() == 0:
        app.group_1.create(Group(name="Школа", header="Номер 2", footer="Номер 3"))
    app.group_1.edit_group(group)
    new_groups = app.group_1.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

# def test_edit_group(app):
#     old_groups = app.group_1.get_group_list()
#     app.group_1.edit_group(Group(footer="New footer"))
#     new_groups = app.group_1.get_group_list()
#     assert len(old_groups) == len(new_groups)