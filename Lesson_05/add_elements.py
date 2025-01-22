from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/add_remove_elements/")

add_el = driver.find_element(By.CSS_SELECTOR, "[onclick='addElement()']")
add_el.click()
add_el.click()
add_el.click()

delete = driver.find_elements(By.CSS_SELECTOR, "[onclick='deleteElement()']")

print(len(delete))

sleep(5)
