import functools
import hashlib
from flask import session, redirect, url_for


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if "username" not in session:
            return redirect(url_for("auth.login"))

        return view(**kwargs)
    return wrapped_view




def hash_password(password):
    sha_signature = hashlib.sha256(password.encode()).hexdigest()
    return sha_signature