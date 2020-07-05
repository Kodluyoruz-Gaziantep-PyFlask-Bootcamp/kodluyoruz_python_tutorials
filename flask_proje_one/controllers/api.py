from flask import jsonify, Blueprint
from flask.views import MethodView

from libraries.app_functions import login_required
from libraries.db_helper import get_db

api_bp = Blueprint('api', __name__, url_prefix='/api')
class UsersApi(MethodView):
    decorators = [login_required]

    def get(self):
        db = get_db()
        cr = db.cursor()
        sql = "SELECT * FROM users"
        cr.execute(sql)
        user_items = cr.fetchall()

        return jsonify({
            "users" : user_items
        })

api_bp.add_url_rule('/users/', view_func=UsersApi.as_view('users'))