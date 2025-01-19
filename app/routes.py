from app import app
from flask_login import current_user, login_user
import sqlalchemy as sa
from flask import render_template



from app import db
from app.models import User


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return "111"
    else:
        return '222'
        # return redirect(url_for('index'))
    # form = LoginForm()
    # if form.validate_on_submit():
    # user = db.session.scalar(
    #     sa.select(User).where(User.username == form.username.data))
    # if user is None or not user.check_password(form.password.data):
    #     flash('Invalid username or password')
    #     return redirect(url_for('login'))
    # login_user(user, remember=form.remember_me.data)
    # return redirect(url_for('index'))
    # return render_template('login.html', title='Sign In', form=form)

@app.route('/second')
def second_page():
    return render_template('second.html', title='Home')