import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait

# 驱动管理
ChromeIns = ChromeDriverManager().install()

driver = webdriver.Chrome(service=Service(ChromeIns))
driver.get("https://www.baidu.com")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "#chat-textarea").send_keys("周星驰")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,"#chat-submit-button").click()
driver.quit()