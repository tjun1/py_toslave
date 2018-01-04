from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

# driver = webdriver.Chrome()
# driver.get("https://www.google.co.jp")
# driver.find_element_by_id("lst-ib").send_keys("selenium")
# driver.find_element_by_id("lst-ib").send_keys(Keys.ENTER)

driver = webdriver.Chrome()
driver.get("http://www.its-kenpo.or.jp/")
driver.find_element_by_link_text("健康増進・保健施設").click()
driver.find_element_by_link_text("保養施設").click()
driver.find_element_by_link_text("直営・通年・夏季保養施設").click()
driver.find_element_by_link_text("WEB申請メニュー画面").click()
sleep(3)
driver.close()

