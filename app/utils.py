from decorator import decorator
from flask import session
from flask import redirect
from flask import request
from app.models.user import UserModel

@decorator
def login_required(f, *args, **kwargs):
    if request.cookies.get('user_id'):
        user_id = request.cookies.get('user_id')
        user = UserModel.query.get(user_id)
        session['user_info'] = {
            'user_id': user.id,
            'name': user.name,
            'email': user.email
        }
        return f(*args, **kwargs)
    else:
        try:
            session['user_info']
        except KeyError:
            return redirect('/')
    
    return f(*args, **kwargs)