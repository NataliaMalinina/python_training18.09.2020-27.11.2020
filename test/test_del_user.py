from model.params_for_user import Parameters


def test_del_user(app):
    if app.user.count() == 0:
        app.user.fill(Parameters(firstname= "тест", bday="0", bmonth="-"))
    old_user = app.user.get_user_list()
    app.user.del_user()
    new_user = app.user.get_user_list()
    assert len(old_user) - 1 == len(new_user)