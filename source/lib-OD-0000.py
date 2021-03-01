#%%
# https://github.com/FinanceData/OpenDartReader
import OpenDartReader
import pandas as pd

API_key = ''
dart = OpenDartReader(API_key) 

#%%
dart.company('005930')
dart.company_by_name('삼성전자')

#%%
dart.find_corp_code('005930')
dart.find_corp_code('삼성전자')

#%%
dart.list_date_ex('2020-01-03')
dart.list('005930', start='1900')

#%%
dart.report('005930', '임원', '2018')
dart.report('005930', '직원', '2018')
dart.report('005930', '배당', '2018')
dart.report('005930', '최대주주', '2018')
dart.report('005930', '소액주주', '2018')

#%%
dart.major_shareholders('005930')
dart.major_shareholders_exec('005930')

#%%
dart.finstate('005930', 2018)
dart.finstate_all('005930', 2018)

#%%
rcept_no = dart.finstate('005930', 2018).rcept_no[0]
rcept_no = dart.finstate_all('005930', 2018).rcept_no[0]
dart.sub_docs(rcept_no)
dart.attach_doc_list(rcept_no)
dart.attach_file_list(rcept_no)

#%%
rcept_no = dart.finstate('005930', 2018).rcept_no[0]
attaches = dart.attach_file_list(rcept_no)
attaches_query = attaches.query('type=="excel"')

file_name = attaches_query.file_name.values[0]
url = attaches.query('type=="excel"').url.values[0]
dart.retrieve(url, file_name)

sheet_names = pd.ExcelFile(file_name).sheet_names
pd.read_excel(file_name, sheet_name=sheet_names[7])
