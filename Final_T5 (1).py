#!/usr/bin/python
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

@route('/best_stocks', method='GET')
def get_best_stocks():
    industry=request.query.industry
    findStr={"Industry":industry}
    return read_document(findStr)
  
def read_document(document):
    try:
        result=collection.find(document,{"Ticker":1,"Industry":2,"Shares Outstanding":3,"50-Day Simple Moving Average":4,"Sector":5,"_id":0}).limit(5)
        #print(list(result))
        return (json_util.dumps(list(result)))
    except Exception as ve:
        abort(400, str(ve))
        return False
    else:
        return True
            
if __name__ == '__main__':
   #app.run(debug=True)
   run(host='localhost', port=8080)
        