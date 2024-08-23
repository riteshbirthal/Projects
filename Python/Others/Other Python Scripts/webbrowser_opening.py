from selenium import webdriver
import time
while True:
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.youtube.com")
    actions = webdriver.ActionChains(driver)
    actions.move_by_offset(400, 400).perform()
    # # actions.click()
    time.sleep(10)
    actions.move_by_offset(-200, -200).perform()
    driver.close()
#1895, 14
#950, 650