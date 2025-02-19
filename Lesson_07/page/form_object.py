from selenium.webdriver.common.by import By


class FormObject:
    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self._driver.implicitly_wait(4)
        self._driver.fullscreen_window()

    def first_name(self, term):
        self._driver.find_element(By.CSS_SELECTOR, "[name='first-name']").send_keys(term)

    def last_name(self, term):
        self._driver.find_element(By.CSS_SELECTOR, "[name='last-name']").send_keys(term)

    def address(self, term):
        self._driver.find_element(By.CSS_SELECTOR, "[name='address']").send_keys(term)

    def e_mail(self, term):
        self._driver.find_element(By.CSS_SELECTOR, "[name='e-mail']").send_keys(term)

    def phone(self, term):
        self._driver.find_element(By.CSS_SELECTOR, "[name='phone']").send_keys(term)

    def zip_code(self, term):
        self._driver.find_element(By.CSS_SELECTOR, "[name='zip-code']").send_keys(term)

    def city(self, term):
        self._driver.find_element(By.CSS_SELECTOR, "[name='city']").send_keys(term)

    def country(self, term):
        self._driver.find_element(By.CSS_SELECTOR, "[name='country']").send_keys(term)

    def job_position(self, term):
        self._driver.find_element(By.CSS_SELECTOR, "[name='job-position']").send_keys(term)

    def company(self, term):
        self._driver.find_element(By.CSS_SELECTOR, "[name='company']").send_keys(term)
        self._driver.find_element(By.CSS_SELECTOR, ".btn.btn-outline-primary.mt-3").click()

    def color_red(self, par):
        color = self._driver.find_element(By.ID, par).value_of_css_property("color")
        return color

    def color_green(self, par):
        color = self._driver.find_element(By.ID, par).value_of_css_property("color")
        return color
