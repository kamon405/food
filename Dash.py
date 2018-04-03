
# coding: utf-8

# In[1]:

import _pickle as cPickle
import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import dash_table_experiments as dt
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import json
import datetime
import pandas as pd
import plotly
import io
import os
import copy



from flask import Flask, jsonify, abort, request, make_response, url_for, g
import uuid
import random
import base64
from werkzeug.contrib.fixers import ProxyFix

from sklearn.linear_model import LogisticRegression

# initialization
app = Flask(__name__)
app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy dog'
app.config['HOST'] = '127.0.0.1'
app.config['DATABASE'] = 'web'
app.config['USER_NAME'] = 'root'
app.config['PASSWORD'] = 'root'

logreg = cPickle.load(open('nonprofit_classifier.pkl', 'rb'))

@app.route('/')
def api_root():
  return "Welcome"

@app.route('/nonprofit', methods=['GET'])
def classify():
    al = request.args['al']
    X = float(al)
    y = logreg.predict(X)

    obj = {"window":"type-0"}
    
    if y == 0:
       obj = {"window":"type-0"}
    elif y == 1:
        obj =  {"window":"type-1"}

    return jsonify(obj)



if __name__ == '__main__':
    app.run(host = '0.0.0.0', port=10015, debug= True)


# In[ ]:



