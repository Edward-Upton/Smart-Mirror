import flask
from flask import request, make_response, render_template
import requests
import json

DEBUG = True
APP = flask.Flask(__name__)
APP.config.from_object(__name__))

@APP.route('/', methods=['GET', 'POST'])
def home():
    return render_template()

if __name__ == "__main__":
    APP.run(host='0.0.0.0', port=80, debug=DEBUG)