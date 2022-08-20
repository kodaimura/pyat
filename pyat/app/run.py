from flask import Flask, Blueprint, redirect
from flask_jwt_extended import (
    JWTManager,
    create_access_token, 
    set_access_cookies, 
    unset_access_cookies, 
    verify_jwt_in_request,
    jwt_required,
    current_user,
)

from views.user_view import bp_user

app = Flask(__name__, static_folder="static", template_folder="templates")
app.register_blueprint(bp_user)

app.config["JWT_SECRET_KEY"] = "super-secret"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = 2592000
app.config["JWT_TOKEN_LOCATION"] = ["cookies"]
app.config["JWT_COOKIE_SECURE"] = False #localのみFalse

jwt = JWTManager(app)


@app.get("/")
@jwt_required()
def index():
    return current_user["user_name"]


# return jwt sub
@jwt.user_identity_loader
def user_identity_lookup(user):
    return user["user_id"]

@jwt.additional_claims_loader
def add_claims_to_access_token(user):
    return {
        "user_id": user["user_id"],
        "user_name": user["user_name"]
    }

@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    return {
        "user_id": jwt_data["user_id"],
        "user_name": jwt_data["user_name"]
    }

@jwt.unauthorized_loader
def custom_unauthorized_response(_err):
    return redirect("login")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)