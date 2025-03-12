from selenium.webdriver.common.by import By


class ShopObject:
    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://www.saucedemo.com/")
        self._driver.implicitly_wait(4)
        self._driver.fullscreen_window()

    def start_page(self, user_name, password):
        self._driver.find_element(By.ID, "user-name").send_keys(user_name)
        self._driver.find_element(By.ID, "password").send_keys(password)
        self._driver.find_element(By.ID, "login-button").click()

    def main_page(self):
        self._driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        self._driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        self._driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

    def cart(self):
        self._driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        self._driver.find_element(By.ID, "checkout").click()

    def checkout(self, first_name, last_name, index):
        self._driver.find_element(By.ID, "first-name").send_keys(first_name)
        self._driver.find_element(By.ID, "last-name").send_keys(last_name)
        self._driver.find_element(By.ID, "postal-code").send_keys(index)
        self._driver.find_element(By.ID, "continue").click()

    def total(self):
        total = self._driver.find_element(By.CSS_SELECTOR, ".summary_total_label").text
        return total
