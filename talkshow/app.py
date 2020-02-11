from flask import Flask
from talkshow.ext import db
from talkshow.ext import cli
from talkshow.blueprints import talks
from talkshow.blueprints import api

def create_app():
    app = Flask(__name__)
    cli.configure(app) 
    db.configure(app)
    api.configure(app)
    talks.configure(app)
    return app