# import library
from bs4 import BeautifulSoup
import requests
import os
from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
os.chmod("/Users/oscarolsen/Documents/Harvard/SophmoreSpring/CS50/final/chromedriver", 755)

driver = webdriver.Chrome("/Users/oscarolsen/Documents/Harvard/SophmoreSpring/CS50/final/chromedriver")

driver.get("https://www.varsom.no/en/avalanche-bulletins/forecast/Trollheimen/")
# #time.sleep(5000)
# driver.find_element_by_id("didomi-notice-agree-button").click()
# #time.sleep(5)
more_buttons = driver.find_element_by_class_name("avalanche-rose")
# more_buttons = driver.find_element_by_class_name("risk-avalanche")
more_buttons_value = more_buttons.get_attribute('value')
# #time.sleep(5)
print("more buttons: ", more_buttons_value)

# # Request to website and download HTML contents
#url='https://meteofrance.com/meteo-montagne/chamonix/740562'
#url="<div class="col-xs-6 col-sm-4 col-md-8">2 - Medium</div>"

# url="https://www.varsom.no/en/avalanche-bulletins/forecast/Indre%20Troms/"
# url2="https://www.varsom.no/en/avalanche-bulletins/forecast/Trollheimen/"
# req=requests.get(url2)
# content=req.text
# # print(content[9000:20000])
# # id = "didomi-notice-agree-button" ol-xs-6 col-sm-4 col-md-8

# soup=BeautifulSoup(content,'html.parser')
# risk_block =soup.find("div", {"class" : "col-xs-6 col-sm-4 col-md-8"})
# risk_block_text = risk_block.text
# print(risk_block_text)

# #'div', class_="modal modal-avalanche"