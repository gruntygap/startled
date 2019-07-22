from flask import Flask, request, abort
from performances import performances

app = Flask(__name__)
app.register_blueprint(performances)
