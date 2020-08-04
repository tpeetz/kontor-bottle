# -*- coding: utf-8 -*-
import pymongo
import sessionDAO
import userDAO
import comics
#import library
import bottle
import cgi
import re


__author__ = 'tpeetz'

app = bottle.Bottle()


def index():
    cookie = bottle.request.get_cookie("session")
    username = sessions.get_username(cookie)
    return bottle.template('kontor', dict(username=username))


def show_signup():
    return bottle.template("signup", dict(username="", 
                                          password="",
                                          password_error="",
                                          email="", 
                                          username_error="", 
                                          email_error="",
                                          verify_error =""))


def process_signup():
    email = bottle.request.forms.get("email")
    username = bottle.request.forms.get("username")
    password = bottle.request.forms.get("password")
    verify = bottle.request.forms.get("verify")

    # set these up in case we have an error case
    errors = {'username': cgi.escape(username), 'email': cgi.escape(email)}
    if validate_signup(username, password, verify, email, errors):

        if not users.add_user(username, password, email):
            # this was a duplicate
            errors['username_error'] = "Username already in use. Please choose another"
            return bottle.template("signup", errors)

        session_id = sessions.start_session(username)
        print(session_id)
        bottle.response.set_cookie("session", session_id)
        bottle.redirect("/welcome")
    else:
        print("user did not validate")
        return bottle.template("signup", errors)


def show_login():
    return bottle.template('login', dict(username="", password="", login_error=""))

def process_login():
    username = bottle.request.forms.get("username")
    password = bottle.request.forms.get("password")

    print("user submitted ", username, "pass ", password)

    user_record = users.validate_login(username, password)
    if user_record:
        # username is stored in the user collection in the _id key
        session_id = sessions.start_session(user_record['_id'])

        if session_id is None:
            bottle.redirect("/internal_error")

        cookie = session_id

        # Warning, if you are running into a problem whereby the cookie being set here is
        # not getting set on the redirect, you are probably using the experimental version of bottle (.12).
        # revert to .11 to solve the problem.
        bottle.response.set_cookie("session", cookie)

        bottle.redirect("/")

    else:
        return bottle.template("login", dict(username=cgi.escape(username), password="", login_error="Invalid Login"))


def process_logout():
    cookie = bottle.request.get_cookie("session")
    sessions.end_session(cookie)
    bottle.response.set_cookie("session", "")
    bottle.redirect("/")


def send_stylesheet(filename):
    return bottle.static_file(filename, root='.', mimetype='text/css') 


def setup_routing(app):
    app.route('/', 'GET', index)
    app.route('/signup', 'GET', show_signup)
    app.route('/signup', 'POST', process_signup)
    app.route('/login', 'GET', show_login)
    app.route('/login', 'POST', process_login)
    app.route('/logout', 'GET', process_logout)
    app.route('/css/<filename:re:.*\.css>', 'GET', send_stylesheet)


# validates that the user information is valid for new signup, return True of False
# and fills in the error string if there is an issue
def validate_signup(username, password, verify, email, errors):
    USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
    PASS_RE = re.compile(r"^.{3,20}$")
    EMAIL_RE = re.compile(r"^[\S]+@[\S]+\.[\S]+$")

    errors['username_error'] = ""
    errors['password_error'] = ""
    errors['verify_error'] = ""
    errors['email_error'] = ""

    if not USER_RE.match(username):
        errors['username_error'] = "invalid username. try just letters and numbers"
        return False

    if not PASS_RE.match(password):
        errors['password_error'] = "invalid password."
        return False
    if password != verify:
        errors['verify_error'] = "password must match"
        return False
    if email != "":
        if not EMAIL_RE.match(email):
            errors['email_error'] = "invalid email address"
            return False
    return True


setup_routing(app)

connection = pymongo.MongoClient("mongodb://localhost")
database = connection.kontor

users = userDAO.UserDAO(database)
sessions = sessionDAO.SessionDAO(database)

comics_plugin = comics.Plugin(app, database, sessions)
#library_plugin = library.Plugin(app, database, sessions)

bottle.run(app, host="localhost", port=9000, debug=True, reloader=True)
