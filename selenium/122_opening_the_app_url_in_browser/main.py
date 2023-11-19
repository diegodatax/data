from selenium import webdriver

driver = webdriver.Firefox()

driver.maximize_window()
URL = "https://tutorialsninja.com/demo"
driver.get(URL)