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
time.sleep(1)
browser.find_element_by_xpath("//*[@id='general-information-section']/div[2]/div/div[7]/div/div[1]/a/i").click()
obj = browser.switch_to.alert
time.sleep(1)
obj.find_element_by_xpath("//*[@id='id_code']").send_keys("ABC123")
obj.find_element_by_xpath("//*[@id='select2-id_shop-container']").send_keys("Default shop")
obj.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/form/div/div/button[1]").click()