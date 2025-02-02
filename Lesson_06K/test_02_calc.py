
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
driver.fullscreen_window()

field = driver.find_element(By.CSS_SELECTOR, "#delay")
field.click()
field.clear()
field.send_keys("45")

driver.find_element(By.XPATH, '//span[text()="7"]').click()
driver.find_element(By.XPATH, '//span[text()="+"]').click()
driver.find_element(By.XPATH, '//span[text()="8"]').click()
driver.find_element(By.XPATH, '//span[text()="="]').click()

start = time.time()
disp = driver.find_element(By.CSS_SELECTOR, ".screen").text
waiter = (WebDriverWait(driver, 50).
          until_not(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.screen'), disp)))
end = time.time()
time_wait = int(end - start)


def test_time_wait():
    assert time_wait == 45


def test_result():
    screen = driver.find_element(By.CLASS_NAME, 'screen').text
    assert screen == '15'
