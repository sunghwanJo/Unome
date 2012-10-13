from flask import Flask, render_template, session, request, redirect,url_for, flash
from flask_oauth import OAuth
import oauth2 as oauth

app = Flask(__name__)
oauth = OAuth()

app.secret_key='DEVELOPE KEY'
consumer_key = 'dih0GsM4wQMZU9AfxgmQ'
consumer_secret= 'AbcQIjh1xDQvrVgqn39LmV9KK2SYyAWTGzVodTaZO90'


twitter = oauth.remote_app('twitter',
    base_url='https://api.twitter.com/1/',
    request_token_url='https://api.twitter.com/oauth/request_token',
    access_token_url='https://api.twitter.com/oauth/access_token',
    authorize_url='https://api.twitter.com/oauth/authorize',
    consumer_key=consumer_key,
    consumer_secret=consumer_secret
)

@twitter.tokengetter
def get_twitter_token(token=None):
    return session.get('twitter_token')

@app.route('/')
def main_view():
	return render_template('index.html')

@app.route('/twitter_login', methods={'POST', 'GET'})
def login():
	print '------- Login -------'	
	return twitter.authorize(callback=url_for('oauth_authorized', next=request.args.get('next') or request.referrer or None))

@app.route('/oauth-athorized')
@twitter.authorized_handler
def oauth_authorized(resp):
	print '-------OAuth Authorized Phase-------'
	next_url = request.args.get('next') or url_for('main_view')
	if resp is None:
		flash(u'You denied the request to sign in.')
		return redirect(next_url)
		
	session['twitter_token'] = (
		resp['oauth_token'],
		resp['oauth_token_secret']
	)
	
	session['twitter_user'] = resp['screen_name']
	
	flash('You were signed in as %s' % resp['screen_name'])
	return redirect(next_url)


if __name__=='__main__':
	app.run(debug=True, host='0.0.0.0', port=2074)
	
