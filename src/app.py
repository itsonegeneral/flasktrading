from flask import Flask,jsonify, request
from flask.json import load
from jugaad_data.nse import NSELive
import socket

app = Flask(__name__)

@app.route('/',methods = ['GET'])
def home():
    n = NSELive()
    q = n.stock_quote("HDFC")
    if request.method == 'GET':
        data = "hello"
        return jsonify({'info':q['info'],'priceInfo':q['priceInfo']})


@app.route('/stocks/<stock>',methods = ['GET'])
def home2(stock="ITC"):
    n = NSELive()
    q = n.stock_quote(stock)
    if request.method == 'GET':
        try:
            return jsonify({'info':q['info'],'priceInfo':q['priceInfo']})
        except:
            return jsonify({'message':'Not Found'})


@app.route('/stocks/tick/<stock>',methods = ['GET'])
def tickData(stock="ITC"):
    print("tickdata " + stock)
    n = NSELive()
    if request.method == 'GET':
        q = n.tick_data(stock)
        return jsonify(q)
       #return jsonify({'info':q['info'],'priceInfo':q['priceInfo']})

@app.route('/markets/all-markets',methods=['GET'])
def getMarketState():
    n = NSELive()
    res = {}
    all_indices = n.all_indices()
    for idx in all_indices['data']:
        res[idx['index']] = idx['last']
        print("{} - {}".format(idx['index'], idx['last']))
    return jsonify({ 'status':'success', 'data':res})

@app.route('/index/<arg>', methods=['GET'])
def getIndexLive(arg="NIFTY 50"):
    n = NSELive()
    print(arg)
    index = n.live_index(arg)
    return jsonify({ 'status':'success', 'data':index})

@app.route('/options/<index>',methods = ['GET'])
def derivatives(index="NIFTY"):
    n = NSELive()
    q = n.index_option_chain(index)
    print(q['records']['expiryDates'])
    if request.method == 'GET':
        data = "hello"
        return jsonify({'data': q})


@app.route('/loadcheck',methods=['GET'])
def checkLoadBalancing():
    return "Container ID : "+ socket.gethostname()

@app.errorhandler(404)
def internal_error(error):
    return "Not Found"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)

