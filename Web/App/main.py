# -*- coding: utf-8 -*-
"""
Main flask application with all the routes
"""

import firebase as firebase
from flask import Flask, render_template, request, redirect, flash, url_for, session, jsonify
# from flask_bootstrap import Bootstrap
import config
import json
from datetime import datetime
import requests
# import utils
# from yolo import yolo

firebase = firebase.Firebase(config.firebaseConfig)
storage = firebase.storage()
auth = firebase.auth()
database = firebase.database()

app = Flask(__name__)
app.config.from_object(config)
# bootstrap = Bootstrap(app)

# """ HTML to be shown to the unregistered user if they try to access a page only accessible for signed in users """
# ASK_LOGIN_TEXT = "You must be logged in to access this page!<br><a href = '/login'></b>click here to log in</b></a>"
#
# """Error messages to be sent if the user passes in invalid json or error on image processing possibly due to bad data"""
# JSON_ERROR_INVALID_JSON = {"error": "failed to parse json, invalid format"}
# JSON_ERROR_PREDICTION_FAILED = {"error": "failed to process image, try another image"}

if __name__ == '__main__':
    app.run(host="0.0.0.0")
