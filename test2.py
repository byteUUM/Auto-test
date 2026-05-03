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
ChromeIns = ChromeDriverManager().install()
# 创建驱动对象
driver = webdriver.Chrome(service=Service(ChromeIns))
wait = WebDriverWait(driver, 10)
# driver.get("https://www.baidu.com")
# wu = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#chat-textarea")))
# wu.send_keys("罗伯托·贝尼尼")
# wu2 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#chat-submit-button")))
# wu2.click()
# # 搜索完成后进行清理
# wu.clear()
#
# wu.send_keys("火山引擎")
# wu2.click()
# wu.clear()
#
# #回退
# driver.back()
# driver.back()
# text = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#hotsearch-content-wrapper > li:nth-child(1) > a > span.title-content-title"))).text
# print(text)
# driver.quit()
driver.get("https://www.douyin.com/jingxuan")
time.sleep(60)
tj = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#douyin-navigation > div > div.MKOzvYDg.Yr4fQlKQ > div > div:nth-child(1) > div.DlKicC22 > div > div:nth-child(2) > div > div > a")))
tj.click()
# dz = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#sliderVideo > div.E7R0E__S.playerContainer.hide-animation-if-not-suport-gpu.TkocvtkE > div > div.vqN35AZ4.basePlayerContainer.xg5nzy2Q.chapterPlayerStyle.MediaNotSupportStyle.lowPopup > div.i2VIB6P0 > div > div > div.zqe4B9aR.WU6dkKao > div:nth-child(2) > div > div.UIQajZAR > div > svg")))
# dz.click()
time.sleep(10)
body = driver.find_element(By.TAG_NAME, 'body')
for i in range(0,10):
    ActionChains(driver).send_keys("z").perform()
    body.send_keys(Keys.ARROW_DOWN)
    # ActionChains(driver).send_keys(Keys.ARROW_DOWN).perform()
    time.sleep(1)
time.sleep(15)
driver.quit()