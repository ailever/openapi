from urllib.request import urlopen, Request
import xmltodict, json, os
import pandas as pd

code = '035420'
url = f"http://asp1.krx.co.kr/servlet/krx.asp.XMLSise?code={code}"
request = Request(url)
request.get_method = lambda: 'GET'
response = urlopen(request).read().decode('utf-8')
stock = json.loads(json.dumps(xmltodict.parse(response[1:-1])))

if os.path.isfile(f'{code}.csv'):
    df = pd.read_csv(f'{code}.csv', thousands = ',').drop('Unnamed: 0', axis=1)
    realtime = pd.DataFrame(data={'date':[stock['stockprice']['@querytime']], 'price':[stock['stockprice']['TBL_StockInfo']['@CurJuka']]})
    df.append(realtime).to_csv(f'{code}.csv')
else:
    pd.DataFrame(data={'date':[stock['stockprice']['@querytime']], 'price':[stock['stockprice']['TBL_StockInfo']['@CurJuka']]}).to_csv(f'{code}.csv')
