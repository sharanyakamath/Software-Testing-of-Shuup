from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
browser = webdriver.Chrome()
browser.get("http://127.0.0.1:8000/sa/login/?next=/sa/") 
time.sleep(1)
username = browser.find_element_by_id("id_username")
password = browser.find_element_by_id("id_password")
username.send_keys("palak")
password.send_keys("palak123")
login_attempt = browser.find_element_by_xpath("//*[@type='submit']")
login_attempt.submit()
time.sleep(1)
browser.get("http://127.0.0.1:8000/sa/campaigns/basket/new/")

browser.find_element_by_xpath("//*[@id='id_base-name']").send_keys('mplace')
browser.find_element_by_xpath("//*[@id='id_base-public_name__en']").send_keys('mplace')
browser.find_element_by_xpath("//*[@id='id_base-basket_line_text']").send_keys('support')
browser.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/form/div/div/button[1]").click()
