import json
from bson import json_util
import bottle
from bottle import route, run, request, abort
import datetime
from bson import json_util
from pymongo import MongoClient

connection = MongoClient('localhost', 27017)
db = connection['market']
collection = db['stocks']

@route('/info', method='GET')
def get_info():
    tickers=request.query.tickers
    print(tickers)
    tickers=tickers.split(",")
    getString={"Ticker":{"$in":tickers}}
    return read_doc(getString)
  
def read_doc(doc):
  try:
    result=collection.find(doc)
    return (json_util.dumps(list(result)))
  except Exception as ve:
      abort(400, str(ve))
      return False
  else:
    return True
  
if __name__ == '__main__':
   #app.run(debug=True)
   run(host='localhost', port=8080)
        
        