from flask import Flask, request, abort
from app.performances import performances

srv = Flask(__name__)
srv.register_blueprint(performances)
