import functools
import hashlib
from flask import current_app, session, redirect, url_for


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if "user_id" not in session:
            return redirect(url_for("auth.login"))

        return view(**kwargs)
    return wrapped_view


def hash_password(password):
    sha_signature = hashlib.sha256( current_app.config["PASSWORD_HASH_KEY"].encode() + password.encode()).hexdigest()
    return sha_signature