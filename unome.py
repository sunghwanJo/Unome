# -*- coding:utf-8 -*-
from flask import Flask, render_template, session, request, redirect,url_for, flash, g
from flask.ext.sqlalchemy import SQLAlchemy
from twitter import *
from twitter import __get_tweets
from unome_utils import TweetAnalyzer
from models import User

# configuration
SECRET_KEY = 'development key'
HOST = '0.0.0.0'
PORT = 2074
DEBUG = True
DATABASE_URI = 'sqlite:////tmp/flask-oauth.db'

# 만약 처음 DB실행시
# db.create_all() 실행
# setip flask
app = Flask(__name__)
app.debug = DEBUG
app.secret_key = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
db = SQLAlchemy(app)

@app.before_request
def before_request():
    g.user = None
    if 'user_id' in session:
        g.user = User.query.get(session['user_id'])

@app.after_request
def after_request(response):
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
        __get_tweets()
        return render_template('index.html', tweets = g.tweets)    
    return render_template('index.html')

@app.route('/get_tweet')
def get_timeline():

    return redirect(request.referrer or url_for('main_view'))

@app.route('/twitter_login', methods={'POST', 'GET'})
def login():
	return twitter.authorize(callback=url_for('oauth_authorized', 
        next=request.args.get('next') or request.referrer or None))

@app.route('/oauth-athorized')
@twitter.authorized_handler
def oauth_authorized(resp):
    print '-------OAuth Authorized Phase-------'
    next_url = url_for('unome_view')
    if resp is None:
        flash(u'You denied the request to sign in.')
        return redirect(next_url)
	
    user = User.query.filter_by(name=resp['screen_name']).first()

    if user is None:
        user = User(resp['screen_name'])
        db.session.add(user)

    user.oauth_token = resp['oauth_token']
    user.oauth_secret = resp['oauth_token_secret']
    db.session.commit()

    session['user_id'] = user.id
    flash('You were signed in')
    return redirect(next_url)

@app.route('/twtest')
def test():
    A = TweetAnalyzer()
    A.start_analyzer()
    print 
    return A.analyze_tweet('조성환 입니다.')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(request.referrer or url_for('main_view'))

@app.route('/unome')
def unome_view():
    if g.user:
        __get_tweets()
    return render_template('unome.html')


# App start
if __name__=='__main__':
    app.run(host=HOST, port=PORT)
	
