from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
options.add_argument("--headless")

# https://sites.google.com/a/chromium.org/chromedriver/downloads
driver = webdriver.Chrome("chromedriver.exe", options=options)
driver.implicitly_wait(5)
driver.get("[URL]")
driver.maximize_window()
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '[XPATH]'))).click()

bs = BeautifulSoup(driver.page_source, 'html.parser')
print(bs.prettify())

# https://www.w3schools.com/cssref/css_selectors.asp
bs.select('[CSS SELECTOR]')
bs.select_one('[CSS SELECTOR]')
bs.find_all('[Tag]', {'[Attr]':'[Value]'})
bs.find('[Tag]', {'[Attr]':'[Value]'})

driver.quit()
