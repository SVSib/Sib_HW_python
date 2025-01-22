from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.maximize_window()
driver.get("http://the-internet.herokuapp.com/inputs")

input_fild = driver.find_element(By.CSS_SELECTOR, "input")
input_fild.send_keys("1000")

sleep(2)

input_fild.clear()

sleep(1)

input_fild.send_keys("999")

sleep(5)
