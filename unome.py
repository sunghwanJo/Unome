# -*- coding:utf-8 -*-
from flask import Flask, render_template, session, request, redirect,url_for, flash, g
from twitter import *
from twitter import __get_tweets
from flask.ext.sqlalchemy import SQLAlchemy

# configuration
SECRET_KEY = 'development key'
HOST = '0.0.0.0'
PORT = 2074
DEBUG = True
DATABASE_URI = 'sqlite:////tmp/unome.db'

# setip flask
app = Flask(__name__)
app.debug = DEBUG
app.secret_key = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI

@app.route('/')
def index():
    return render_template('index.html')

# App start
if __name__=='__main__':
    app.run(host=HOST, port=PORT)
    import unome_utils
