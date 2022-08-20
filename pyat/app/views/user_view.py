from flask import (
	Blueprint, 
	render_template, 
	request, 
	redirect, 
	make_response,
	jsonify
)
import hashlib
from flask_jwt_extended import (
	create_access_token,
	set_access_cookies,
	unset_access_cookies
)


import models.user_model as um

bp_user = Blueprint("bp_user", __name__, template_folder="templates")


@bp_user.get("/login")
def login_page():
	return render_template("login.html")


@bp_user.get("/signup")
def signup_page():
	return render_template("signup.html")


@bp_user.get("/logout")
def logout():
    response = make_response(redirect("login"))
    unset_access_cookies(response)
    return response


@bp_user.post("/login")
def login():
	username = request.form["username"]
	password = request.form["password"]

	user = um.select_by_username(username)
	if (len(user) == 0 or
		user[0]["password"] != hashlib.sha256(password.encode()).hexdigest()):

		return render_template(
			"login.html",
			error= "UsernameまたはPasswordが異なります。"
		)

	access_token = create_access_token(identity=user[0])
	response = make_response(redirect("/"))
	set_access_cookies(response, access_token)

	return response


@bp_user.post("/signup")
def signup():
	username = request.form["username"]
	password = request.form["password"]

	if len(um.select_by_username(username)) != 0:
		return render_template(
			"signup.html",
			error="Usernameが既に使われています"
		)

	hpass = hashlib.sha256(password.encode()).hexdigest()
	um.signup(username, hpass)
	return redirect("login")