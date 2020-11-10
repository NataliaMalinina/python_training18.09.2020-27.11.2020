import re
from model.params_for_user import Parameters


def test_all_fields_for_user(app, db):
    user_list_from_main_page = sorted(app.user.get_user_list(), key=Parameters.id_or_max)
    user_list_from_db = sorted(db.get_user_list(), key=Parameters.id_or_max)
    assert len(user_list_from_db) == len(user_list_from_main_page)
    for element_id in range(0, len(user_list_from_db)):
        assert user_list_from_main_page[element_id].id == user_list_from_db[element_id].id
        assert user_list_from_main_page[element_id].lastname == user_list_from_db[element_id].lastname
        assert user_list_from_main_page[element_id].firstname == user_list_from_db[element_id].firstname
        assert user_list_from_main_page[element_id].address == user_list_from_db[element_id].address
        assert user_list_from_main_page[element_id].all_emails_from_home_page == \
               merge_emails_like_on_home_page(user_list_from_db[element_id])
        assert user_list_from_main_page[element_id].all_phones_from_home_page == \
               merge_phones_like_on_home_page(user_list_from_db[element_id])


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