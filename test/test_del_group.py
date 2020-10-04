from model.group import Group

def test_delete_first_group(app):
    if app.group_1.count() == 0:
        app.group_1.create(Group(name= "тест"))
    app.group_1.delete_first_group()
