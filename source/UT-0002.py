from urllib.request import urlopen
from bs4 import BeautifulSoup

response = urlopen('[URL]')
bs = BeautifulSoup(response.read().decode('utf-8'), 'html.parser')
print(bs.prettify())

# https://www.w3schools.com/cssref/css_selectors.asp
bs.select('[CSS SELECTOR]')
bs.select_one('[CSS SELECTOR]')
bs.find_all('[Tag]', {'[Attr]':'[Value]'})
bs.find('[Tag]', {'[Attr]':'[Value]'})
