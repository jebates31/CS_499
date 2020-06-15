import json
import datetime
from bson import json_util
from pymongo import MongoClient

connection = MongoClient('localhost', 27017)
db = connection['market']
collection = db['stocks']

def create(document):
    try:
        result=collection.insert(document)
    except ValidationError as ve:
      abort(400,str(ve))
      return False
    else:
      return True
    
def main():
    myDoc = {
        "Ticker" : "BB",
        "Profit Margin" : 0.237,
        "Institutional Ownership" : 0.950,
        "EPS growth past 5 years" : 0.160,
        "Total Debt/Equity" : 0.60,
        "Current Ratio" : 4,
        "Return on Assets" : 0.090,
        "Sector" : "Healthcare",
        "P/S" : 2.60,
        "Change from Open" : -0.0450,
        "Performance (YTD)" : 0.3000,
        "Performance (Week)" : 0.0040,
        "Quick Ratio" : 2.5,
        "Insider Transactions" : -0.2503,
        "P/B" : 4.65,
        "EPS growth quarter over quarter" : -0.39,
        "Payout Ratio" : 0.262,
        "Performance (Quarter)" : 0.0828,
        "Forward P/E" : 15.10,
        "P/E" : 18.0,
        "200-Day Simple Moving Average" : 0.1162,
        "Shares Outstanding" : 339,
        "Earnings Date" : datetime.datetime(2013,11,14,21,30),
        "52-Week High" : -0.6044,
        "P/Cash" : 7.50,
        "Change" : -0.0248,
        "Analyst Recom" : 2.6,
        "Volatility (Week)" : 0.0277,
        "Country" : "USA",
        "Return on Equity" : 0.282,
        "50-Day Low" : 0.0828,
        "Price" : 51.44,
        "50-Day High" : -0.0644,
        "Return on Investment" : 0.1765,
        "Shares Float" : 335.21,
        "Dividend Yield" : 0.0090,
        "EPS growth next 5 years" : 0.0943,
        "Industry" : "Medical Laboratories & Research",
        "Beta" : 1.5,
        "Sales growth quarter over quarter" : -0.041,
        "Operating Margin" : 0.187,
        "EPS (ttm)" : 2.68,
        "PEG" : 2.27,
        "Float Short" : 0.008,
        "52-Week Low" : 0.4378,
        "Average True Range" : 0.86,
        "EPS growth next year" : 0.1194,
        "Sales growth past 5 years" : 0.048,
        "Company" : "Agilent Technologies Inc.",
        "Gap" : 0,
        "Relative Volume" : 0.79,
        "Volatility (Month)" : 0.0168,
        "Market Cap" : 17356.8,
        "Volume" : 1847978,
        "Gross Margin" : 0.512,
        "Short Ratio" : 1.03,
        "Performance (Half Year)" : 0.1439,
        "Relative Strength Index (14)" : 46.51,
        "Insider Ownership" : 0.001,
        "20-Day Simple Moving Average" : -0.0172,
        "Performance (Month)" : 0.0063,
        "P/Free Cash Flow" : 19.63,
        "Institutional Transactions" : -0.0074,
        "Performance (Year)" : 0.4242,
        "LT Debt/Equity" : 0.56,
        "Average Volume" : 2569.36,
        "EPS growth this year" : 0.147,
        "50-Day Simple Moving Average" : -0.0055}
    print create(myDoc)
main()

      