from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.saucedemo.com/")
driver.fullscreen_window()
driver.implicitly_wait(10)

login = driver.find_element(By.ID, "user-name")
login.click()
login.send_keys("standard_user")

password = driver.find_element(By.ID, "password")
password.click()
password.send_keys("secret_sauce")

driver.find_element(By.ID, "login-button").click()

driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
driver.find_element(By.ID, "checkout").click()

first_name = driver.find_element(By.ID, "first-name")
first_name.click()
first_name.send_keys("Сергей")

last_name = driver.find_element(By.ID, "last-name")
last_name.click()
last_name.send_keys("Сибиряков")

index = driver.find_element(By.ID, "postal-code")
index.click()
index.send_keys("699090")

driver.find_element(By.ID, "continue").click()

total = driver.find_element(By.CSS_SELECTOR, ".summary_total_label").text


def test_total():
    assert total == "Total: $58.29"
    print(total)


driver.quit()

test_total()
