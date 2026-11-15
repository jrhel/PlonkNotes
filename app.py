from flask import Flask
from flask import session
from flask import render_template
from flask import redirect
from flask import request
import config
import db_connection_handler
import user

app = Flask(__name__)
db_connection_handler.verify_database()
app.secret_key = config.get_session_key()

@app.route("/")
def index():
    if "username" in session.keys():
        return redirect("/user_page")
    else:
        potential_error_message = session.pop("message", None)
        return render_template("index.html", message = potential_error_message)

@app.route("/sign_up")
def sign_up():
    potential_error_message = session.pop("message", None)
    return render_template("sign_up.html", message = potential_error_message)

@app.route("/create_account", methods=["POST"])
def create_account():
    username = request.form["username"]
    password1 = request.form["password1"]
    password2 = request.form["password2"]
    if not username or not password1 or not password2:
        error_message = "One or more fields were ampty. Please, make sure to fill in all the fields!"
        session["message"] = error_message
        return redirect("/sign_up")
    if password1 != password2:
        error_message = "Sorry, the passwords didn't match. Please, try again!"
        session["message"] = error_message
        return redirect("/sign_up")
    elif user.check_available_username(username):
        user.create_user(username, password1)
        session["username"] = username
        return redirect("/user_page")
    else:
        error_message = f"The username {username} is not available. Please, try another one!"
        session["message"] = error_message
        return redirect("/sign_up")

@app.route("/sign_in", methods=["POST"])
def sign_in():
    username = request.form["username"]
    password = request.form["password"]
    if user.verify_user(username, password):
        session["username"] = username
        return redirect("/user_page")
    else:
        error_message = "The username or password was incorrect!"
        session["message"] = error_message
        return redirect("/")

@app.route("/user_page")
def user_page():
    return render_template("user.html")

@app.route("/sign_out", methods=["POST"])
def sign_out():
    session.clear()
    return redirect("/")