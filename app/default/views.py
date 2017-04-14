from flask import Blueprint
from flask import request
from flask import redirect
from flask import session
from flask import render_template
from app.models.user import UserModel
from app.extensions import db
from flask import make_response
import datetime

default_blueprint = Blueprint('default', __name__, url_prefix='/')


@default_blueprint.route('')
def index():
    return render_template('default.html')


@default_blueprint.route('signup', methods=['POST'])
def signup():
    
    message = ''
    
    email = request.form['email']
    password = request.form['password']
    name = request.form['name']
    
    user = UserModel.query.filter(UserModel.email == email).first()
    if user:
        message = 'Sorry, that email is already taken.'
    else:
        db.session.add(UserModel(email=email, name=name, password=password))
        db.session.commit()
        message = 'Congrats. You are on facebook now. Please login again.'
        
    return render_template('signup.html', message=message)


@default_blueprint.route('login', methods=['POST'])
def login():
    message = ''
        
    email = request.form['email']
    password = request.form['password']
    remember_me = request.form.get('remember_me')
    
    user = UserModel.query.filter(UserModel.email == email, UserModel.password == password).first()
    
    if user:
        session['user_info'] = {
            'user_id': user.id,
            'name': user.name,
            'email': user.email
        }
        if remember_me:
            expire_date = datetime.datetime.now()
            expire_date = expire_date + datetime.timedelta(days=90)
            resp = make_response(redirect('/main'))
            resp.set_cookie('user_id', str(user.id), expires=expire_date)
            return resp
    else:
        message = 'Invalid login..'
    
    return render_template('login.html', message=message)

