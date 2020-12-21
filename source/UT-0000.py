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
driver.find_elements_by_css_selector("[CSS SELECTOR]")[0].click(); time.sleep(3)
driver.find_elements_by_css_selector("[CSS SELECTOR]")[0].click(); time.sleep(3)
driver.find_elements_by_css_selector("[CSS SELECTOR]")[0].click(); time.sleep(3)

bs = BeautifulSoup(driver.page_source, 'html.parser')
selected_list = bs.select('[CSS SELECTOR]')
for v in selected_list:
    v.select('[CSS SELECTOR]')
    v.select('[CSS SELECTOR]')
    v.select('[CSS SELECTOR]')

driver.quit()
