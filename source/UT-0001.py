import requests
from bs4 import BeautifulSoup

response = requests.get("[URL]")
bs = BeautifulSoup(response.text, 'html.parser')
print(bs.prettify())

# https://www.w3schools.com/cssref/css_selectors.asp
bs.select('[CSS SELECTOR]')
bs.select_one('[CSS SELECTOR]')
bs.find_all('[Tag]', {'[Attr]':'[Value]'})
bs.find('[Tag]', {'[Attr]':'[Value]'})
