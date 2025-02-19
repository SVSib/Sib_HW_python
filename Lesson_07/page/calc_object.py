from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.by import By


class CalcObject:
    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self._driver.implicitly_wait(4)
        self._driver.fullscreen_window()

    def delay(self, term):
        second = self._driver.find_element(By.CSS_SELECTOR, "#delay")
        second.clear()
        second.send_keys(term)

    def keyboard(self, key):
        self._driver.find_element(By.XPATH, '//span[text()="'+key+'"]').click()

    def timer(self):
        start = time.time()
        disp = self._driver.find_element(By.CSS_SELECTOR, ".screen").text
        WebDriverWait(self._driver, 50).until_not(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.screen'), disp))
        end = time.time()
        time_wait = int(end - start)
        return time_wait

    def result(self):
        screen = self._driver.find_element(By.CLASS_NAME, 'screen').text
        return screen
