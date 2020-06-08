import json
import datetime
from bson import json_util
from pymongo import MongoClient

connection = MongoClient('localhost', 27017)
db = connection['market']
collection = db['stocks']

def delete(findDocument):
  try:
    result=collection.remove(findDocument)
    print(json_util.dumps(list(result)))
  except VaidationError as ve:
    abort(400, str(ve))
    print 'Error:', ve
def main():
  findDocument = {"Ticker":"BRLI"}
  print delete(findDocument)
main()    

    

