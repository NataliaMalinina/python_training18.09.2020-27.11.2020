from model.group import Group


def test_edit_group(app):
    if app.group_1.count() == 0:
        app.group_1.create(Group(name="Школа", header="Номер 2", footer="Номер 3"))
    app.group_1.edit_group(Group(name="Грибоедова"))

def test_edit_group(app):
    app.group_1.edit_group(Group(footer="New footer"))