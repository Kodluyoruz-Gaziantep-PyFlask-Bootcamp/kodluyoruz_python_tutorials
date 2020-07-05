from flask import Blueprint, render_template, session, redirect, url_for, jsonify, request, abort
from flask.views import View, MethodView

from libraries.app_functions import login_required
from libraries.db_helper import get_db

website_bp = Blueprint('website', __name__, url_prefix='/')

@website_bp.route("/")
def posts():
    db = get_db()
    cr = db.cursor()

    params = []
    sql = "SELECT * FROM posts LEFT JOIN users ON posts.user_id=users.user_id"

    q = request.args.get("query")
    if q:
        sql += " WHERE post_content LIKE ? OR post_title LIKE ? OR post_summary LIKE ?"
        params.append('%'+q+'%')
        params.append('%'+q+'%')
        params.append('%'+q+'%')

    cr.execute(sql,tuple(params))

    post_items = cr.fetchall()
    #print(post_items)
    return render_template("posts.html", post_items=post_items)


@website_bp.route("/post/<id>")
def show_post(id):
    db = get_db()
    cr = db.cursor()
    cr.execute("SELECT * FROM posts LEFT JOIN users ON posts.user_id=users.user_id WHERE post_id=?", (id,))
    post_item = cr.fetchone()

    if not post_item:
        abort(404)

    return render_template("show_post.html", post_item=post_item)

class ShowUsers(View):
    methods = ['GET', 'POST']

    def dispatch_request(self):
        db = get_db()
        cr = db.cursor()
        sql = "SELECT * FROM users"
        cr.execute(sql)
        user_items = cr.fetchall()

        return render_template('users.html',user_items=user_items)

# x = login_required(ShowUsers.as_view('users'))
website_bp.add_url_rule('/users/', view_func=ShowUsers.as_view('users'))


