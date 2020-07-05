from flask import Blueprint, request, render_template, session, jsonify
from libraries.db_helper import get_db
from libraries.app_functions import login_required
from libraries.exceptions import ValidationException
from libraries.forms import NewPostForm, EditPostForm

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

@admin_bp.route("/")
@login_required
def dashboard():
    return render_template("admin_dashboard.html")

@admin_bp.route("/post_new",methods=["GET","POST"])
@login_required
def post_new():
    data = {"status": "success", "error_message": ""}

    new_post_form = NewPostForm()

    if new_post_form.is_submitted():
        if new_post_form.validate():
            try:
                post_title = new_post_form.post_title.data
                post_summary = new_post_form.post_summary.data
                post_content = new_post_form.post_content.data

                db = get_db()
                cr = db.cursor()

                sql = "INSERT INTO posts(post_title,post_summary,post_content,user_id) VALUES(?,?,?,?)"
                cr.execute(sql, (post_title, post_summary, post_content, session["user_id"]))
                db.commit()
            except ValidationException as e:
                data["status"] = "error"
                data["error_message"] = str(e)
            except Exception as e:
                data["status"] = "error"
                data["error_message"] = str(e)
            finally:
                if data["status"] == "error":
                    errorHtml = render_template("errors_messages.html", form=new_post_form, data=data)
                    data["error_message"] = errorHtml
        elif request.method=="POST":
            data["status"] = "error"
            data["error_message"] = render_template("errors_messages.html", form=new_post_form, data=data)

        return jsonify(data)


    return render_template("admin_post_new.html", new_post_form=new_post_form, data=data)



@admin_bp.route("/post_edit/<post_id>",methods=["GET","POST"])
@login_required
def post_edit(post_id):
    data = {"status": "success", "error_message": ""}

    db = get_db()
    cr = db.cursor()

    post_edit_form = EditPostForm()
    if post_edit_form.is_submitted():
        if post_edit_form.validate():
            try:
                post_title = post_edit_form.post_title.data
                post_summary = post_edit_form.post_summary.data
                post_content = post_edit_form.post_content.data

                sql = "UPDATE posts SET post_title=?, post_summary=?, post_content=? WHERE post_id=?"
                cr.execute(sql, (post_title, post_summary, post_content, post_id))
                db.commit()
            except ValidationException as e:
                data["status"] = "error"
                data["error_message"] = str(e)
            except Exception as e:
                data["status"] = "error"
                data["error_message"] = "Bilinmeyen bir hata oluştu"
            finally:
                if data["status"] == "error":
                    errorHtml = render_template("errors_messages.html", form=post_edit_form, data=data)
                    data["error_message"] = errorHtml
        else:
            data["status"] = "error"
            data["error_message"] = render_template("errors_messages.html", form=post_edit_form, data=data)

        return jsonify(data)

    sql = "SELECT * FROM posts WHERE post_id=?"
    cr.execute(sql,(post_id,))
    post_item = cr.fetchone()

    return render_template("admin_post_edit.html", post_item=post_item, post_edit_form=post_edit_form)


@admin_bp.route("/posts")
@login_required
def admin_posts():
    db = get_db()
    cr = db.cursor()

    sql = "SELECT * FROM posts JOIN users ON posts.user_id=users.user_id WHERE posts.user_id=?"
    cr.execute(sql, (str(session["user_id"]),))
    post_items = cr.fetchall()


    return render_template("admin_posts.html", post_items=post_items)