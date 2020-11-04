from model.params_for_user import Parameters
import random


def test_del_user(app, db, check_ui):
    if len(db.get_user_list()) == 0:
        app.user.fill(Parameters(firstname="тест", bday="0", bmonth="-"))
    old_user = db.get_user_list()
    user = random.choice(old_user)
    app.user.del_user_by_id(user.id)
    new_user = db.get_user_list()
    assert len(old_user) - 1 == len(new_user)
    old_user.remove(user)
    assert sorted(old_user, key=Parameters.id_or_max) == sorted(new_user, key=Parameters.id_or_max)
    if check_ui:
        assert sorted(new_user, key=Parameters.id_or_max) == sorted(app.user.get_user_list(),
                                                                         key=Parameters.id_or_max)
