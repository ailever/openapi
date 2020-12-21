from selenium import webdriver
from bs4 import BeautifulSoup
import time

options = webdriver.ChromeOptions()
options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
options.add_argument("--headless")

# https://sites.google.com/a/chromium.org/chromedriver/downloads
driver = webdriver.Chrome("chromedriver.exe", options=options)
driver.implicitly_wait(5)
driver.get("[URL]")
driver.maximize_window()
# https://www.w3schools.com/cssref/css_selectors.asp
driver.find_elements_by_css_selector("[CSS SELECTOR]")[0].click(); time.sleep(3)
driver.find_elements_by_css_selector("[CSS SELECTOR]")[0].click(); time.sleep(3)
driver.find_elements_by_css_selector("[CSS SELECTOR]")[0].click(); time.sleep(3)

bs = BeautifulSoup(driver.page_source, 'html.parser')
bs.select('[CSS SELECTOR]')
bs.find_all('[CSS SELECTOR]')

driver.quit()
