from model.params_for_user import Parameters


def test_edit_user(app):
    old_user = app.user.get_user_list()
    if app.user.count() == 0:
        app.user.fill(Parameters(firstname= "тест", bday="0", bmonth="-"))
    app.user.edit_user((Parameters(firstname="Thane", middlename="Omar Kennedy", lastname="Snider",
        company="Calhoun Carter Trading", address="Distinctio Amet no", home="Cillum veniam eveni",
        mobile="Dolor sint perspicia", work="Voluptas voluptatibu", email="giwige@mailinator.net",
        byear="2000", bday="5", bmonth="September", new_group="[none]")))
    new_user = app.user.get_user_list()
    assert len(old_user) == len(new_user)

