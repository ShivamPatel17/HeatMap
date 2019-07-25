#!/usr/bin/env python
import selenium
import urllib
from urllib import *
import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
import BeautifulSoup
from BeautifulSoup import *

print ("hi")

driver = webdriver.Chrome("//home//shivam//Heatmap//chromedriver")
driver.set_page_load_timeout(30)
driver.get("https:////factfinder.census.gov//faces//nav//jsf/pages//index.xhtml")
#driver.maximize_window()
#print("Maximized window /n")
driver.implicitly_wait(100)
zipcode =driver.find_element_by_id("cfsearchtextboxmain").send_keys("08807")
time.sleep(2)
print("zip code entered")
go_button = driver.find_elements_by_xpath("//*[@id=\"cfmainsearchform\"]/a")[0]
go_button.click()
time.sleep(2)
print("Go!")
data_link = driver.find_element_by_link_text('Demographic and Housing Estimates (Age, Sex, Race, Households and Housing, ...)')
time.sleep(2)
data_link.click()

print("at the data pageee")
url = driver.current_url

driver.get(url)
driver.implicitly_wait(100)
time.sleep(2)
html = driver.page_source
soup = BeautifulSoup(html)
table = soup.find('table', id = "data")
m65row = table.find(id = 'r25').parent
print(m65row.contents[1].string)
driver.close()
print("FINISHED")
