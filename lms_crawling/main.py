# coding=<utf-8>
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 

from bs4 import BeautifulSoup
import requests
import time

import os
import json

# 데이터 가져오기. my-config.json은 실행파일과 같은 위치에 있어야함
# "my-config.json"
#   id: lms id
#   password: lms password
#   lecture: 강의자료를 가져올 강의 제목  ex) "자료구조(005)"

with open(os.path.join(os.path.dirname(__file__), 'my-config.json'), 'r', encoding="utf-8") as f:
    json_data = json.load(f)
    id = json_data["id"]
    pwd = json_data["password"]
    lecture = json_data["lecture"]

# Selenium 설정. 묵시적 대기는 6초
driver = webdriver.Chrome('chromedriver.exe')
driver.implicitly_wait(6)

# lms 홈페이지와 강의 목록 페이지 링크
lms_url = "https://lms.knu.ac.kr/"
lecture_list_url = "https://lms.knu.ac.kr/ilos/mp/course_register_list_form.acl"

# lms homepage 접속
driver.get(url=lms_url)

# lms login page 접속
driver.find_element_by_css_selector('.header_login').click()

elem = driver.find_element_by_css_selector('#usr_id')
elem.send_keys(id)
elem = driver.find_element_by_css_selector('#usr_pwd')
elem.send_keys(pwd, Keys.RETURN)

# lms 강의 목록 페이지 접속
driver.get(url=lecture_list_url)
driver.find_element_by_css_selector('#onceLecture').click()

# 내가 원하는 강의를 찾아서 접속
elems = driver.find_elements_by_css_selector('.content-container>div span')
for (i, elem) in enumerate(elems):
    if (lecture == elem.text):
        elem.click()
        break

# 강의 자료 게시판 이동
driver.find_element_by_css_selector('#menu_lecture_material').click()
elems = driver.find_elements_by_css_selector('.left')
count = len(elems)

# innerHTML은 해당 elem의 내부 html을 가지고 outerHTML은 해당 elem을 포함한 html을 가진다.
# print(elems[0].get_attribute('outerHTML')) 

# 처음에는 클릭과 뒤로가기로 구현하려 했으나, 오류가 발생하여 onclick 속성의 링크를 따와서 이동하는 식으로 구현
post_links = []
for (i, elem) in enumerate(elems):
    soup = BeautifulSoup(elem.get_attribute('outerHTML'), 'html.parser')
    
    link = 'https://lms.knu.ac.kr' + soup.td['onclick'].split("'")[1]
    post_links.append(link)
    

for url in post_links:
    driver.get(url)
    elem = driver.find_element_by_css_selector('a[title="첨부파일 다운로드"]')
    
    print(elem.text)
    elem.click()   # 다운로드 클릭
    time.sleep(1)  # 너무 빠르게 링크를 벗어나 다운로드가 되지 않는 상황을 방지

time.sleep(4)
driver.quit()