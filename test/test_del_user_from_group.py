import random
from model.params_for_user import Parameters
from model.group import Group


def test_del_user_of_group(app, db, check_ui):
    if len(db.get_user_list()) == 0:
        app.user.fill(Parameters(firstname="тест", lastname="Bbshko", address="gfgfhv jfjd12", bday="0", bmonth="-"))
    if len(db.get_group_list()) == 0:
        app.group_1.create(Group(name="тест"))
    list_of_group = db.get_group_list()
    name_of_group = random.choice(list_of_group)
    app.user.delete_from_group(name_of_group)
    if check_ui:
        assert sorted(list_of_group, key=Parameters.id_or_max) == sorted(app.group_1.get_group_list(),
                                                                         key=Parameters.id_or_max)


