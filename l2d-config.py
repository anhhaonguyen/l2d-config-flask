from numpy import *
from scipy.optimize import leastsq
import math, json, socket

from flask import Flask, request
app = Flask(__name__)

# ================================================================================= 
@app.route('/')
def index():
    return ''

# ================================================================================= 
@app.route('/create', methods=['POST'])
def create():
	return 'create ok'
# ================================================================================= 
@app.route('/update', methods=['POST'])
def update():
	return 'update ok'
# =================================================================================
app.run(host='localhost', port=5000)