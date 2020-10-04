from model.params_for_user import Parameters


def test_del_user(app):
    if app.user.count() == 0:
        app.user.fill(Parameters(firstname= "тест", bday="0", bmonth="-"))
    app.user.del_user()