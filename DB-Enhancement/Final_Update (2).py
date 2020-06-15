import json
import datetime
from bson import json_util
from pymongo import MongoClient

connection = MongoClient('localhost', 27017)
db = connection['market']
collection = db['stocks']

def update (findDocument, newDocument):
  try:
    result=collection.update(findDocument,{"$set":newDocument})
    print(json_util.dumps(list(result)))
  except ValidationError as ve:
    abort(400,str(ve))
    print 'Error:', ve
    return False
    
def main():
  findDocument = {"Ticker":"BB", "Volume":1847978}
  newDocument = {"Volume":3500000}
  print update(findDocument,newDocument)
  
main()
  

