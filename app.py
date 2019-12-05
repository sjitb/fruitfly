# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 22:38:52 2019

@author: satrajit
"""
import json
from flask import Flask
from fruitpal_helper import dataClient

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>The Fruit API</h1>'

@app.route('/api/<name>')
def indexname(name):
    return json.dumps({"about": "<h1>The {} API</h1>".format(name)}) 

@app.route('/api/overhead/<string:commodity>', methods=['GET'])
def get_overhead(commodity):

    dc = dataClient()
    response = dc.getDataForAPI(commodity)
    return json.dumps(response)

if __name__=='__main__':
    app.run(debug=True)