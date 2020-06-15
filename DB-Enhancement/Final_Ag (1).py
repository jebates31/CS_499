import json
import datetime
from bson import json_util
from pymongo import MongoClient

connection = MongoClient('localhost', 27017)
db = connection['market']
collection = db['stocks']

def Ag(sector):
  try:
    result=collection.aggregate([
      {"$match": {"Sector": sector } },
      {"$group": {"_id":"$Industry", "total": {"$sum": "$Outstanding Shares"}}}
    ])
    return (list(result))
  except Exception as ve:
      print ve
  else:
      return True
def main():
      print Ag ("Basic Materials")
main()
