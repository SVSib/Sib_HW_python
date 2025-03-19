from selenium.webdriver.common.by import By


class FormObject:
    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self._driver.implicitly_wait(4)
        self._driver.fullscreen_window()

    def first_name(self, term: str):
        """
				Эта функция выбирает поле "Имя".
		"""
        self._driver.find_element(By.CSS_SELECTOR, "[name='first-name']").send_keys(term)

    def last_name(self, term: str):
        """
        		Эта функция выбирает поле "Фамилия".
        """
        self._driver.find_element(By.CSS_SELECTOR, "[name='last-name']").send_keys(term)

    def address(self, term: str):
        """
                Эта функция выбирает поле "Адрес".
        """
        self._driver.find_element(By.CSS_SELECTOR, "[name='address']").send_keys(term)

    def e_mail(self, term: str):
        """
                Эта функция выбирает поле "Эмэил".
        """
        self._driver.find_element(By.CSS_SELECTOR, "[name='e-mail']").send_keys(term)

    def phone(self, term: str):
        """
                Эта функция выбирает поле "Телефон".
        """
        self._driver.find_element(By.CSS_SELECTOR, "[name='phone']").send_keys(term)

    def zip_code(self, term: str):
        """
                Эта функция выбирает поле "Zip-code".
        """
        self._driver.find_element(By.CSS_SELECTOR, "[name='zip-code']").send_keys(term)

    def city(self, term: str):
        """
                Эта функция выбирает поле "Город".
        """
        self._driver.find_element(By.CSS_SELECTOR, "[name='city']").send_keys(term)

    def country(self, term: str):
        """
                Эта функция выбирает поле "Страна".
        """
        self._driver.find_element(By.CSS_SELECTOR, "[name='country']").send_keys(term)

    def job_position(self, term: str):
        """
                Эта функция выбирает поле "Должность".
        """
        self._driver.find_element(By.CSS_SELECTOR, "[name='job-position']").send_keys(term)

    def company(self, term: str):
        """
                Эта функция выбирает поле "Компания и нажимает кнопку Submit".
        """
        self._driver.find_element(By.CSS_SELECTOR, "[name='company']").send_keys(term)
        self._driver.find_element(By.CSS_SELECTOR, ".btn.btn-outline-primary.mt-3").click()

    def set_color(self, par: str) -> str:
        """
                Эта функция возвращает цвет поля.
        """
        color = self._driver.find_element(By.ID, par).value_of_css_property("color")
        return color
