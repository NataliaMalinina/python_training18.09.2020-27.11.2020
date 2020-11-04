from model.group import Group
import random


def test_edit_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group_1.create(Group(name="Школа", header="Номер 2", footer="Номер 3"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group_1.edit_group_by_id(group.id, Group(name="Room"))
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups.remove(group)
    old_groups = db.get_group_list()
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group_1.get_group_list(),
                                                                 key=Group.id_or_max)