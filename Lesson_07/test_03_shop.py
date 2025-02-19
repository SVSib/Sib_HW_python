from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from page.shop_object import ShopObject


def test_shop():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    shop_object = ShopObject(browser)
    shop_object.start_page("standard_user", "secret_sauce")
    shop_object.main_page()
    shop_object.cart()
    shop_object.checkout("Сергей", "Сибиряков", "669090")
    shop_object.total()
    assert shop_object.total() == "Total: $58.29"
