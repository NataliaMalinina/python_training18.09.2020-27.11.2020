import re
from model.params_for_user import Parameters


def test_all_fields_for_user(app, db):
    user_spisok_from_main_page = app.user.get_user_list()
    user_spisok_from_db = db.get_user_list()
    assert sorted(user_spisok_from_main_page, key=Parameters.id_or_max) == user_spisok_from_db


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(parameters):
    return "\n".join(filter(lambda x: x != "",
                            (map(lambda x: clear(x), filter(lambda x: x is not None,
                                [parameters.home, parameters.mobile, parameters.work, parameters.phone2])))))

def merge_emails_like_on_home_page(parameters):
    return "\n".join(filter(lambda x: x != "",
                            (map(lambda x: clear(x), filter(lambda x: x is not None,
                                [parameters.email, parameters.email2, parameters.email3])))))