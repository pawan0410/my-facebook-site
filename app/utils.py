from decorator import decorator
from flask import session
from flask import redirect

@decorator
def login_required(f, *args, **kwargs):
    try:
        session['user_info']
    except KeyError:
        return redirect('/')
            
    return f(*args, **kwargs)