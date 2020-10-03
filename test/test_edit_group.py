from model.group import Group


# def test_edit_group_name(app):
#     app.group_1.modify_first_group(Group(name="Школа"))
#     app.session.logout()

def test_edit_group(app):
    app.group_1.edit_group(Group(name="Школа", header="Номер 2", footer="Номер 3"))
