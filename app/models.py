from app import db
from hashlib import md5

ROLE_USER = 0
ROLE_ADMIN = 1


class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nickname = db.Column(db.String(64), index = True, unique = True)
    email = db.Column(db.String(120), index = True, unique = True)
    role = db.Column(db.SmallInteger, default = ROLE_USER)
    posts = db.relationship('Post', backref = 'author', lazy = 'dynamic')
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime)

    @staticmethod
    def make_unique_nickname(nickname):
        if User.query.filter_by(nickname=nickname).first() == None:
            return nickname
        
        # If nickname exists then it changes it with number
        version = 2
        while True:
            new_nickname = nickname + str(version)
            if User.query.filter_by(nickname = new.nickname).first() == None:
                break
            version += 1
        return new_nickname


    # Return true unless user not allowed to authenticate
    def is_authenticated(self):
        return True

    # Returns False for a banned user
    def is_active(self):
        return True

    # Return true for fake users not supposed to login
    def is_anonymous(self):
        return False

    # Generate unique id for user 
    def get_id(self):
        return unicode(self.id)

    def avatar(self, size):
        return 'http://www.gravatar.com/avatar' + md5(self.email).hexdigest() + '?d=mm&s' + str(size)

    # Used fro debugging and structures how to print objects fo this class
    def __repr__(self):
        return '<User %r>' % (self.nickname)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String(140))
    timestamp = db. Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post %r>' % (self.body)