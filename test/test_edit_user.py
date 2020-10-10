from model.params_for_user import Parameters


def test_edit_user(app):
    old_user = app.user.get_user_list()
    user = Parameters(firstname="Thane", lastname="Snider")  #middlename="Omar Kennedy", lastname="Snider",
    #     company="Calhoun Carter Trading", address="Distinctio Amet no", home="Cillum veniam eveni",
    #     mobile="Dolor sint perspicia", work="Voluptas voluptatibu", email="giwige@mailinator.net",
    #     byear="2000", bday="5", bmonth="September", new_group="[none]")
    user.id = old_user[0].id
    if app.user.count() == 0:
        app.user.fill(Parameters(firstname= "тест", bday="0", bmonth="-"))
    app.user.edit_user(user)
    new_user = app.user.get_user_list()
    assert len(old_user) == len(new_user)
    old_user[0] = user
    assert sorted(old_user, key=Parameters.id_or_max) == sorted(new_user, key=Parameters.id_or_max)



