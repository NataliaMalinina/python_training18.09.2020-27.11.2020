

def test_edit_user(app):
    app.session.login(username="admin", password="secret")
    app.add_user.edit_user()
    app.session.logout()