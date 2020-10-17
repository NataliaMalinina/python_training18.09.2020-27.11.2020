import re


def test_all_fields_for_user(app):
    user_from_home_page = app.user.get_user_list()[0]
    user_from_edit_page = app.user.get_user_info_from_edit_page(0)
    assert user_from_home_page.firstname == clear(user_from_edit_page.firstname)
    assert user_from_home_page.lastname == clear(user_from_edit_page.lastname)
    assert user_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(user_from_edit_page)
    assert user_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(user_from_edit_page)


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