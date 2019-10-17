from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

auth = HTTPBasicAuth()

users = {
    "alvaro@bestateless.com": generate_password_hash("this is not my password")
}


@auth.verify_password
def verify_password(username, password):
    print("users:{}".format(users.get(username)))
    if username in users:
        return check_password_hash(users.get(username), password)
    return False


def __init__(self):
    self.name = 'authorization_helper'
