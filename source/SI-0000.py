from urllib.parse import urlencode, quote_plus
from urllib.request import urlopen, Request
import json

url = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson'
KEY = 'percent-encoding key'
queryParams = '?' + quote_plus('ServiceKey') + f'={KEY}&' + urlencode({quote_plus('pageNo'):'1',
                                                                       quote_plus('numOfRows'):'10',
                                                                       quote_plus('startCreateDt'):'20200310',
                                                                       quote_plus('endCreateDt'):'20200315',
                                                                       quote_plus('_type'):'json'})

request = Request(url + queryParams)
request.get_method = lambda: 'GET'
response = urlopen(request).read().decode('utf-8')
covid19 = json.loads(response)
