from flask import Blueprint
from flask import request
from flask import redirect
from flask import session
from flask import render_template
from app.models.user import UserModel
from app.extensions import db
from app.utils import login_required

main_blueprint = Blueprint('main', __name__, url_prefix='/main')


@main_blueprint.route('')
@login_required
def index():
    return render_template('main/main.html')