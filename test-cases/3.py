from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
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
browser.get("http://127.0.0.1:8000/sa/orders/") 
time.sleep(1)
browser.find_element_by_xpath(
    "//*[@id='picotable']/div/table/tbody/tr[3]/td[1]/div/label"
).click()
time.sleep(1)
select = Select(browser.find_element_by_xpath("//*[@id='select2-mass-action-select58027449-container']"))
select.select_by_id("select2-mass-action-select58027449-result-9729-mass_action_order_confirmation_pdf")
#browser.find_element_by_xpath("//*[@id='select2-mass-action-select58027449-result-9729-mass_action_order_confirmation_pdf']").click()