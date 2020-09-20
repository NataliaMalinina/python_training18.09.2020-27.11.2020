
class Parameters:
    def __init__(self, firstname, middlename, lastname, nickname, title, company, byear, ayear,
                 address, address2, notes, bday, bmonth, aday, amonth, new_group):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.byear = byear
        self.ayear = ayear
        self.address = address
        self.address2 = address2
        self.notes = notes
        self.bday = bday
        self.bmonth = bmonth
        self.aday = aday
        self.amonth = amonth
        self.new_group = new_group


class Phones:
    def __init__(self, home, mobile, work, fax, phone2):
        self.home = home
        self.mobile = mobile
        self.work = work
        self.fax = fax
        self.phone2 = phone2


class Emails:
    def __init__(self, email, email2, email3, homepage):
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage