from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object('config')
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

from app import views
