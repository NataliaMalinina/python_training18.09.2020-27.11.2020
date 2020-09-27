
def test_del_user(app):
    app.session.login(username="admin", password="secret")
    app.user.del_user()
    app.session.logout()