from model.group import Group


def test_edit_group(app):
    app.session.login(username="admin", password="secret")
    app.redact_group.edit_group(Group(name="Школа", header="Номер №1", footer="Номер №2"))
    app.session.logout()