import datetime
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

# 获取浏览器驱动
ChromeIns = ChromeDriverManager.install()
#创建驱动对象
driver = webdriver.Chrome(service=Service(ChromeIns))
wait = WebDriverWait(driver,10)

#登录测试
driver.get("http://49.235.61.184/?s=user/regInfo.html")

username = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"body > div.body-content-container > div.body-content-formal-container > div.am-g.user-register-container.theme-data-edit-event > div > div > div.am-radius-lg.am-background-white > div > div.am-tabs-bd.am-border-0 > div.am-tab-panel.am-active > form > div.am-form-group.am-form-group-refreshing.am-form-input-material.am-form-error > input")))
username.send_keys("wangwu")
password = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"body > div.body-content-container > div.body-content-formal-container > div.am-g.user-register-container.theme-data-edit-event > div > div > div.am-radius-lg.am-background-white > div > div.am-tabs-bd.am-border-0 > div.am-tab-panel.am-active > form > div.am-form-group.am-form-group-refreshing.am-margin-top-main.am-form-input-material.am-form-error > input")))
password.send_keys("123456")

bk = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"body > div.body-content-container > div.body-content-formal-container > div.am-g.user-register-container.theme-data-edit-event > div > div > div.am-radius-lg.am-background-white > div > div.am-tabs-bd.am-border-0 > div.am-tab-panel.am-active > form > div.am-form-group.am-margin-top-main.am-padding-0 > button")))
bk.click()

driver.quit()