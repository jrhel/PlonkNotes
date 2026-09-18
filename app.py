from flask import Flask
from flask import session
from flask import render_template
from flask import redirect
from flask import request

import user
import db_connection_handler

app = Flask(__name__)
db_connection_handler.verify_database()
# ! Fix secret key !
app.secret_key = "18fd24bf6a2ad4dac04a33963db1c42f"

# The user is rendered the landing page, from where they can log in or sign up, unless they are already signed in, in which case they get redirected to their own user page.
@app.route("/")
def index():
    if "username" in session.keys():
        return redirect("/user_page")
    else:
        return render_template("index.html")

@app.route("/sign_up")
def sign_up():
    return render_template("sign_up.html")

@app.route("/create_account", methods=["POST"])
# The function verifies that the passwords entered on the sign-up page match each other, that the username is not taken, and that all three fields were filled in.
# If not, the sign-up page is rendered again with a message of what went wrong.
# Otherwise, the user information is passed on to the application logic, which handles signing up the user, who is then redirected to their own user page.
def create_account():
    username = request.form["username"]
    password1 = request.form["password1"]
    password2 = request.form["password2"]
    # ! Check to set message separately in session, then redirect to "/" !
    if not username or not password1 or not password2:
        return render_template("sign_up.html", message = "One or more fields were ampty. Please, make sure to fill in all the fields!")
    if password1 != password2:
        return render_template("sign_up.html", message = "Sorry, the passwords didn't match. Please, try again!")
    elif user.check_available_username(username):
        user.create_user(username, password1)
        session["username"] = username
        return redirect("/user_page")
    else:
        availability_message = f"The username {username} is not available. Please, try another one!"
        return render_template("sign_up.html", message = availability_message)

@app.route("/user_page")
def user_page():
    return render_template("user.html")

@app.route("/sign_out", methods=["POST"])
def sign_out():
    session.clear()
    return redirect("/")