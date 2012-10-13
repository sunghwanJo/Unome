from flask import Flask, render_template, session, request, redirect,url_for, flash, g
from flask_oauth import OAuth

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# configuration
SECRET_KEY = 'development key'
DATABASE_URI = 'sqlite:////tmp/flask-oauth.db'
HOST = '0.0.0.0'
PORT = 2074
DEBUG = True

#OAuth configuration
CONSUMER_KEY = 'QdGOizY0OznyHCwL73S2Uw'
CONSUMER_SECRET= 'Pv9CexLxhXmTQauQBEvkA7pHlGz1Kru4we8X9iBVAM'

# setip flask
app = Flask(__name__)
app.debug = DEBUG
app.secret_key = SECRET_KEY
oauth = OAuth()

# Use Twitter API
twitter = oauth.remote_app('twitter',
    base_url='https://api.twitter.com/1/',
    request_token_url='https://api.twitter.com/oauth/request_token',
    access_token_url='https://api.twitter.com/oauth/access_token',
    authorize_url='https://api.twitter.com/oauth/authorize',
    consumer_key=CONSUMER_KEY,
    consumer_secret=CONSUMER_SECRET
)

#setup sqlalchemy
engine = create_engine(DATABASE_URI)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    Base.metadata.create_all(bind=engine)

class User(Base):
    __tablename__ = 'users'
    id = Column('user_id', Integer, primary_key=True)
    name = Column(String(60))
    oauth_token = Column(String(200))
    oauth_secret = Column(String(200))

    def __init__(self, name):
        self.name = name

@app.before_request
def before_request():
    g.user = None
    if 'user_id' in session:
        g.user = User.query.get(session['user_id'])
@app.after_request
def after_request(response):
    db_session.remove()
    return response

@twitter.tokengetter
def get_twitter_token(token=None):
    user = g.user
    if user is not None:
        return user.oauth_token, user.oauth_secret

@app.route('/')
def main_view():
    tweets = None
    if g.user is not None:
    # user login
        return render_template('index.html')
    return render_template('index.html')

@app.route('/twitter_login', methods={'POST', 'GET'})
def login():
	return twitter.authorize(callback=url_for('oauth_authorized', 
        next=request.args.get('next') or request.referrer or None))

@app.route('/oauth-athorized')
@twitter.authorized_handler
def oauth_authorized(resp):
    print '-------OAuth Authorized Phase-------'
    next_url = request.args.get('next') or url_for('main_view')
    if resp is None:
        flash(u'You denied the request to sign in.')
        return redirect(next_url)
	
    user = User.query.filter_by(name=resp['screen_name']).first()

    if user is None:
        user = User(resp['screen_name'])
        db_session.add(user)

    user.oauth_token = resp['oauth_token']
    user.oauth_secret = resp['oauth_token_secret']
    db_session.commit()

    session['user_id'] = user.id
    flash('You were signed in')
    return redirect(next_url)

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(request.referrer or url_for('main_view'))

if __name__=='__main__':
	app.run(host=HOST, port=PORT)
	
