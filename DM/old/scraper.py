import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import bs4
from bs4 import BeautifulSoup


import time


# fh = open('exam_data_new.txt','w')
# st = '\n'
# fh.write(st)
driver = webdriver.Chrome()
driver.get("https://app.cpcbccr.com/ccr/#/caaqm-dashboard-all/caaqm-landing/data/%7B%22state%22:%22Karnataka%22,%22city%22:%22Bengaluru%22,%22station%22:%22site_1556%22%7D")


time.sleep(10)

driver.close()