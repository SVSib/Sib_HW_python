import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
driver.fullscreen_window()

first_name = driver.find_element(By.CSS_SELECTOR, "[name='first-name']")
first_name.click()
first_name.send_keys("Иван")

last_name = driver.find_element(By.CSS_SELECTOR, "[name='last-name']")
last_name.click()
last_name.send_keys("Петров")

address = driver.find_element(By.CSS_SELECTOR, "[name='address']")
address.click()
address.send_keys("Ленина, 55-3")

email = driver.find_element(By.CSS_SELECTOR, "[name='e-mail']")
email.click()
email.send_keys("test@skypro.com")

phone_number = driver.find_element(By.CSS_SELECTOR, "[name='phone']")
phone_number.click()
phone_number.send_keys("+7985899998787")

city = driver.find_element(By.CSS_SELECTOR, "[name='city']")
city.click()
city.send_keys("Москва")

country = driver.find_element(By.CSS_SELECTOR, "[name='country']")
country.click()
country.send_keys("Россия")

job_position = driver.find_element(By.CSS_SELECTOR, "[name='job-position']")
job_position.click()
job_position.send_keys("QA")

company = driver.find_element(By.CSS_SELECTOR, "[name='company']")
company.click()
company.send_keys("SkyPro")

button = driver.find_element(By.CSS_SELECTOR, "[type='submit']")
button.click()

WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#company'), 'SkyPro'))


@pytest.mark.parametrize(
    'creds',
    [
        'zip-code'
    ]
)
def test_color_red(creds):
    par = creds
    color = driver.find_element(By.ID, par).value_of_css_property("color")
    red = "rgba(132, 32, 41, 1)"
    assert color == red


@pytest.mark.parametrize(
    'creds',
    [
        'first-name',
        'last-name',
        'address',
        'e-mail',
        'phone',
        'city',
        'country',
        'job-position',
        'company'
    ]
)
def test_color_green(creds):
    par = creds
    color = driver.find_element(By.ID, par).value_of_css_property("color")
    green = "rgba(15, 81, 50, 1)"
    assert color == green
