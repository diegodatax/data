from selenium import webdriver
import time

driver = webdriver.Firefox()

driver.maximize_window()
URL = "https://selenium143.blogspot.com/"
driver.get(URL)

time.sleep(3)

driver.execute_script("history.go(0)")

"""
https://www.w3schools.com/jsref/met_his_go.asp
"""

time.sleep(3)

driver.quit()