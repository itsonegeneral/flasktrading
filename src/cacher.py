from flask.json import jsonify
from jugaad_data.nse import NSELive
import time
import json

nifty= ['HDFCBANK','SBIN','IOC', 'POWERGRID','RELIANCE',
'HINDUNILVR','DIVISLAB','ICICIBANK','SUNPHARMA','NESTLEIND',
'ASIANPAINT','HDFC','SBILIFE','INFY','ITC','BHARTIARTL','AXISBANK','TITAN',
'TATACONSUM','BAJAJ-AUTO','NTPC','HDFCLIFE','ULTRACEMCO','BRITANNIA',
'GRASIM','KOTAKBANK','TCS','CIPLA','HINDALCO','ADANIPORTS','JSWSTEEL',
'BAJAJFINSV','WIPRO','ONGC','BAJFINANCE','COALINDIA','BPCL','UPL',
'TATACONSUM', 'IOC', 'HDFC',  'NTPC' ,'TATAMOTORS', 'MARUTI', 'INDUSINDBK',
'JSWSTEEL','BPCL','ONGC','ADANIPORTS' ]




def loadNifty():
    print("Refreshing NIfty")
    temp = []
    for i in nifty:
        temp.append(getStockData(i))
    jsonString = json.dumps(temp)
    f = open("data.json", "w")
    f.write(jsonString)
    f.close()



def getStockData(stock="ITC"):
    n = NSELive()
    q = n.stock_quote(stock)
    # print('GETTING STOCK ' + stock)
    # print(q['info']['symbol'])
    return ({'info':q['info'],'priceInfo':q['priceInfo']})


while True:
    loadNifty()
    time.sleep(30)
