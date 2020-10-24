# -*- coding: utf-8 -*-
from model.group import Group
import pytest
from data.add_group import testdata

@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_address_group(app, group):
        old_groups = app.group_1.get_group_list()
        app.group_1.create(group)
        assert len(old_groups) + 1 == app.group_1.count()
        new_groups = app.group_1.get_group_list()
        old_groups.append(group)
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


