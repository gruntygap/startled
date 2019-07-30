from flask import Flask, request, abort
from app.performances import performances

app = Flask(__name__)
app.register_blueprint(performances)
