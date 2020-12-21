from urllib.parse import urlencode, quote_plus
from urllib.request import urlopen, Request
import xmltodict, json
import pandas as pd

code = '035420'
url = f"http://asp1.krx.co.kr/servlet/krx.asp.XMLSise?code={code}"
request = Request(url)
request.get_method = lambda: 'GET'
response = urlopen(request).read().decode('utf-8')
stock = json.loads(json.dumps(xmltodict.parse(response[1:-1])))

stock['stockprice']['@querytime']
stock['stockprice']['TBL_DailyStock']
stock['stockprice']['TBL_AskPrice']
stock['stockprice']['TBL_StockInfo']
stock['stockprice']['TBL_Hoga']
stock['stockprice']['TBL_TimeConclude']
stock['stockprice']['stockInfo']
