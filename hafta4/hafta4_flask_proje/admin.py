from flask import Blueprint,g,request,render_template,session
from db_helper import get_db
from app_functions import login_required

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

@admin_bp.route("/")
@login_required
def dashboard():
    return render_template("admin_dashboard.html")

@admin_bp.route("/post_new",methods=["GET","POST"])
@login_required
def post_new():
    if request.method=="POST":
        post_title = request.form.get("post_title")
        post_summary = request.form.get("post_summary")
        post_content = request.form.get("post_content")

        db = get_db()
        cr = db.cursor()

        sql = "INSERT INTO posts(post_title,post_summary,post_content,user_id) VALUES(?,?,?,?)"
        cr.execute(sql,(post_title,post_summary,post_content,session["user_id"]))
        db.commit()
        return "yazıyı başarıyla kaydettim"

    return render_template("admin_post_new.html")



@admin_bp.route("/post_edit/<post_id>",methods=["GET","POST"])
@login_required
def post_edit(post_id):
    db = get_db()
    cr = db.cursor()

    if request.method=="POST":
        post_title = request.form.get("post_title")
        post_summary = request.form.get("post_summary")
        post_content = request.form.get("post_content")

        sql = "UPDATE posts SET post_title=?, post_summary=?, post_content=? WHERE post_id=?"
        cr.execute(sql,(post_title,post_summary,post_content,post_id))
        db.commit()
        return "yazı başarıyla düzenlendi"

    sql = "SELECT * FROM posts WHERE post_id=?"
    cr.execute(sql,(post_id))
    post_item = cr.fetchone()

    return render_template("admin_post_edit.html", post_item=post_item)


@admin_bp.route("/posts")
@login_required
def admin_posts():
    db = get_db()
    cr = db.cursor()

    sql = "SELECT * FROM posts JOIN users ON posts.user_id=users.user_id WHERE posts.user_id=?"
    cr.execute(sql, (str(session["user_id"])))
    post_items = cr.fetchall()


    return render_template("admin_posts.html", post_items=post_items)