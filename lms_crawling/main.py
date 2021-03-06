# coding=<utf-8>
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 

from bs4 import BeautifulSoup
import requests
import time

import os
import json

driver = webdriver.Chrome('chromedriver.exe')
driver.implicitly_wait(6)

lms_url = "https://lms.knu.ac.kr/"
lecture_list_url = "https://lms.knu.ac.kr/ilos/mp/course_register_list_form.acl"

# lms homepage
driver.get(url=lms_url)

# lms login page
driver.find_element_by_css_selector('.header_login').click()

with open(os.path.join(os.path.dirname(__file__), 'my-config.json'), 'r') as f:
    json_data = json.load(f)
    id = json_data["id"]
    pwd = json_data["password"]

    elem = driver.find_element_by_css_selector('#usr_id')
    elem.send_keys(id)
    elem = driver.find_element_by_css_selector('#usr_pwd')
    elem.send_keys(pwd, Keys.RETURN)

# lms lecture list page
driver.get(url=lecture_list_url)
driver.find_element_by_css_selector('#onceLecture').click()

# lms lecture page
elems = driver.find_elements_by_css_selector('.content-container>div span')
lecture = "자료구조(005)"
for (i, elem) in enumerate(elems):
    if (lecture == elem.text):
        elem.click()
        break

# lecture material page
driver.find_element_by_css_selector('#menu_lecture_material').click()
elems = driver.find_elements_by_css_selector('.left')
count = len(elems)

# innerHTML은 해당 elem의 내부 html을 가지고 outerHTML은 해당 elem을 포함한 html을 가진다.
# print(elems[0].get_attribute('outerHTML')) 

post_links = []
for (i, elem) in enumerate(elems):
    soup = BeautifulSoup(elem.get_attribute('outerHTML'), 'html.parser')
    
    link = 'https://lms.knu.ac.kr' + soup.td['onclick'].split("'")[1]
    post_links.append(link)
    

for url in post_links:
    driver.get(url)
    elem = driver.find_element_by_css_selector('a[title="첨부파일 다운로드"]')
    
    print(elem.text)
    elem.click()
    time.sleep(1)

time.sleep(4)
driver.quit()