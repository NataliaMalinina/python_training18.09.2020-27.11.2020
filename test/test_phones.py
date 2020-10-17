import re


def test_phones_on_home_page(app):
    user_from_home_page = app.user.get_user_list()[0]
    user_from_edit_page = app.user.get_user_info_from_edit_page(0)
    assert user_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(user_from_edit_page)

def test_phones_on_user_view_page(app):
    user_from_view_page = app.user.get_user_from_view_page(0)
    user_from_edit_page = app.user.get_user_info_from_edit_page(0)
    assert user_from_view_page.home == user_from_edit_page.home
    assert user_from_view_page.mobile == user_from_edit_page.mobile
    assert user_from_view_page.work == user_from_edit_page.work


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(parameters):
    return "\n".join(filter(lambda x: x != "",
                            (map(lambda x: clear(x), filter(lambda x: x is not None,
                                [parameters.home, parameters.mobile, parameters.work, parameters.phone2])))))

