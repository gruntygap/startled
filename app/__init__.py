from flask import Flask, request, abort
from app.performances import performances

app = Flask(__name__, static_url_path='')
app.register_blueprint(performances)
