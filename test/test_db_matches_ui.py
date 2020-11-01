from model.group import Group
from model.params_for_user import Parameters

def test_group_list(app, db):
    ui_list = app.group_1.get_group_list()
    def clean(group):
        return Group (id=group.id, name=group.name.strip())
    db_list = map(clean, db.get_group_list())
    assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)

def test_user_list(app, db):
    ui_list = app.user.get_user_list()
    def clean(user):
        return Parameters(id=user.id, firstname=user.firstname.strip(), middlename=user.middlename.strip(),
                            lastname=user.lastname.strip())
    db_list = map(clean, db.get_user_list())
    assert sorted(ui_list, key=Parameters.id_or_max) == sorted(db_list, key=Parameters.id_or_max)
