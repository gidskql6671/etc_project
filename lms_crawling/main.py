from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import requests

driver = webdriver.Chrome('chromedriver.exe')
driver.implicitly_wait(6)

lms_url = "https://lms.knu.ac.kr/"

driver.get(url=lms_url)

driver.find_element_by_css_selector('.header_login').click()

input_login = driver.find_element_by_css_selector('#usr_id')
input_password = driver.find_element_by_css_selector('#usr_pwd')