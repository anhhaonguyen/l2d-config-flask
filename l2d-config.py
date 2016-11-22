from numpy import *
from scipy.optimize import leastsq
import math, json, socket
import os, errno

from flask import Flask, request
app = Flask(__name__)

# ================================================================================= 
@app.route('/')
def index():
    return ''

# ================================================================================= 
@app.route('/create', methods=['POST'])
def create():
    data = request.json
    evo_name = data['name']
    config_file = evo_name + '.json'
    with open(config_file, 'w') as output:
        json.dump(data['config'], output, indent=4, sort_keys=True, separators=(',', ':'))
	return 'create done'
# ================================================================================= 
@app.route('/update', methods=['POST'])
def update():
    data = request.json
    evo_name = data['name']
    config_file = evo_name + '.json'
    with open(config_file, 'w') as output:
        json.dump(data['config'], output, indent=4, sort_keys=True, separators=(',', ':'))
	return 'update done'
# ================================================================================= 
@app.route('/config', methods=['POST'])
def config():
    data = request.json
    evo_name = data['name']
    config_file = evo_name + '.json'
    with open(config_file) as json_data:
        d = json.load(json_data)
        return json.dumps(d)
# ================================================================================= 
@app.route('/delete', methods=['POST'])
def delete():
    data = request.json
    evo_name = data['name']
    config_file = evo_name + '.json'
    try:
        os.remove(config_file)
        return 'delete done'
    except OSError:
        return 'file not exist'
# =================================================================================
app.run(host='localhost', port=5000)