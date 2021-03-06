##перебор всех значение нейм, хэдэр, футер
from model.group import Group
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [
    Group(name=name, header=header, footer=footer)
    for name in ["", random_string("name", 10)]
    for header in ["", random_string("header", 20)]
    for footer in ["", random_string("footer", 15)]
]


@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_address_group(app, group):
        old_groups = app.group_1.get_group_list()
        app.group_1.create(group)
        assert len(old_groups) + 1 == app.group_1.count()
        new_groups = app.group_1.get_group_list()
        old_groups.append(group)
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


