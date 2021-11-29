from flask import Flask,jsonify, request
from flask.json import load
from jugaad_data.nse import NSELive
import time
import threading
import json
import os
import subprocess

process = subprocess.Popen(['python3','cacher.py'],shell=False)
app = Flask(__name__)

@app.route('/',methods = ['GET'])
def home():
    n = NSELive()
    q = n.stock_quote("HDFC")
    if request.method == 'GET':
        data = "hello"
        return jsonify({'info':q['info'],'priceInfo':q['priceInfo']})


@app.route('/<stock>',methods = ['GET'])
def home2(stock="ITC"):
    n = NSELive()
    q = n.stock_quote(stock)
    if request.method == 'GET':
        return jsonify({'info':q['info'],'priceInfo':q['priceInfo']})


@app.route('/nifty/list',methods=['GET'])
def getNiftyStocks():
    f = open("data.json", "r")
    return ({'data':json.load(f)})
    

@app.route('/live/<index>',methods = ['GET'])
def derivatives(index="NIFTY"):
    n = NSELive()
    q = n.index_option_chain(index)
    print(q['records']['expiryDates'])
    if request.method == 'GET':
        data = "hello"
        return jsonify({'data': q})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555)

