#!/usr/bin/env python3
import os
from flask import Flask, request, current_app, g, make_response     # for index return
# from flask import Flask             # for package import
# from flask import request           # for requesting headers for 'Host'
# from flask import current_app       # to access/invoke app_name()
# from flask import g                 # for before_request (determining path)
# from flask import make_response     # for index return

app = Flask(__name__)

@app.before_request 
def app_path():
    g.path = os.request.path.abspath(os.getcwd())

@app.route('/')
def index():
    host = request.headers.get('Host')
    appname = current_app.name
    response_body = f'''
        <h1>The host for this page is {host}</h1>
        <h2>The name of this application is {appname}</h2>
        <h3>The path of this application on the user's device is {g.path}</h3>''', \
        202
    status_code = 200
    headers = {}
    return make_response(response_body, status_code, headers)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
