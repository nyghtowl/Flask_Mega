from flask import render_template
from app import app
from forms import LoginForm

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
def login():
    form = LoginForm()

    # Following command conducts validation processing for submited form
    if form.validate_on_submit():
        flash('Login requested for OpenID="' + form.openid.data + '",remember_me=' + str(form.remember_me.data))
        return redirect('/index')
    return render_template('login.html',
        title = 'Sign In',
        form = form,
        providers = app.config['OPENID_PROVIDERS'])
    
# Loads user from database
@lm.user_loader
def load_user(id):
    return User.query.get(int(id))