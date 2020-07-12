from flask import Blueprint, render_template, session, redirect, url_for, jsonify

from modules.auth.forms import LoginForm

public_bd = Blueprint("public",__name__,url_prefix="/")

@public_bd.route("/")
def main():
    form = LoginForm()
    return render_template("public/main.html",form=form)

