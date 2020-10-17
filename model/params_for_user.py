from sys import maxsize


class Parameters:
    def __init__(self, firstname=None, middlename=None, lastname=None,
                 company=None, address=None, home=None, mobile=None, work=None, phone2=None, email=None,
                 byear=None, bday=None, bmonth=None, new_group=None, id=None, all_phones_from_home_page=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.company = company
        self.address = address
        self.home = home
        self.mobile = mobile
        self.work = work
        self.phone2 = phone2
        self.email = email
        self.byear = byear
        self.bday = bday
        self.bmonth = bmonth
        self.new_group = new_group
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page

    def __repr__(self):
        return "%s: %s %s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id == other.id or self.id is None or other.id is None) \
               and self.firstname == other.firstname and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize