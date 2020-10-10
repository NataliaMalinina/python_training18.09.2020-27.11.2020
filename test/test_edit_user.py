from model.params_for_user import Parameters
from random import randrange

def test_edit_user(app):
    if app.user.count() == 0:
        app.user.fill(Parameters(firstname= "тест", bday="0", bmonth="-"))
    old_user = app.user.get_user_list()
    index = randrange(len(old_user))
    user = Parameters(firstname="Thane", lastname="Snider")  #middlename="Omar Kennedy", lastname="Snider",
    #     company="Calhoun Carter Trading", address="Distinctio Amet no", home="Cillum veniam eveni",
    #     mobile="Dolor sint perspicia", work="Voluptas voluptatibu", email="giwige@mailinator.net",
    #     byear="2000", bday="5", bmonth="September", new_group="[none]")
    user.id = old_user[index].id
    app.user.edit_user_by_index(index, user)
    new_user = app.user.get_user_list()
    assert len(old_user) == len(new_user)
    old_user[index] = user
    assert sorted(old_user, key=Parameters.id_or_max) == sorted(new_user, key=Parameters.id_or_max)



