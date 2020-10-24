from model.params_for_user import Parameters
import random
import string
import json
import os.path
import getopt
import sys
import jsonpickle

try:
    opts, args = getopt.getopt(sys.argv[1:], "u:f:", ["number of users", "file"])
except getopt.GetoptError as err:
    getopt.usege()
    sys.exit(2)

u = 3
f = "data/users.json"

for o, a in opts:
    if o == "-u":
        u = int(a)
    elif o == "-f":
        f = a

def random_user(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_user_digits(prefix, maxlen):
    symbols = string.digits + string.punctuation + " "*6
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [
    Parameters(firstname=random_user("firstname", 10), middlename=random_user("middlename", 10),
    lastname=random_user("lastname", 20), company=random_user("company", 25), address=random_user("address", 31),
        home=random_user_digits("home", 13), mobile=random_user_digits("mobile", 12), work=random_user_digits("work", 15),
            phone2=random_user_digits("phone2", 20), email=random_user("email", 34))
    for i in range(u)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)
with open(file, "w") as bm:
    jsonpickle.set_encoder_options("json", indent=2)
    bm.write(jsonpickle.encode(testdata))

