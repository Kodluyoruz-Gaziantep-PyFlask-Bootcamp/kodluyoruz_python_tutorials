from flask import Flask, g, render_template, Markup, request, session
from db_helper import get_db
from auth import auth_bp
from admin import admin_bp

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.teardown_appcontext
def close_connection(exception):
    print("close_connection")
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route('/hello_world')
def hello_world():
    return 'Hello World!'



@app.route("/")
def posts():
    db = get_db()
    cr = db.cursor()

    params = []
    sql = "SELECT * FROM posts JOIN users ON posts.user_id=users.user_id"

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


@app.route("/post/<id>")
def show_post(id):
    db = get_db()
    cr = db.cursor()
    cr.execute("SELECT * FROM posts JOIN users ON posts.user_id=users.user_id WHERE post_id=?", (id))
    post_item = cr.fetchone()
    print(post_item)
    return render_template("show_post.html", post_item=post_item)





app.register_blueprint(auth_bp)
app.register_blueprint(admin_bp)
if __name__ == '__main__':
    app.run()
