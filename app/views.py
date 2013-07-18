from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db, lm, oid
from forms import LoginForm
from models import User, ROLE_USER, ROLE_ADMIN

@app.route('/')
@app.route('/index')
def index():
    user = { 'nickname': 'Miguel' } # fake user
    posts = [#fake dictionary of posts
    {
        'author': {'nickname':'John'},
        'body': 'Beautiful day in Portland'
    },
    {
        'author': {'nickname':'John'},
        'body': 'The Avengers movie was so cool!'

    }
    ]
    return render_template("index.html", 
        title = 'Home', 
        user = user,
        posts = posts)

@app.route('/login', methods = ['GET', 'POST'])
@oid.loginhandler
def login():
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('index'))

    form = LoginForm()

    # Following command conducts validation processing for submited form
    if form.validate_on_submit():
        flash('Login requested for OpenID="' + form.openid.data + '",remember_me=' + str(form.remember_me.data))
        session['remember_me'] = form.remember_me.data
        return oid.try_login(form.openid.data, ask_for = ['nickname', 'email'])
    return render_template('login.html',
        title = 'Sign In',
        form = form,
        providers = app.config['OPENID_PROVIDERS'])
    
# Loads user from database
@lm.user_loader
def load_user(id):
    return User.query.get(int(id))