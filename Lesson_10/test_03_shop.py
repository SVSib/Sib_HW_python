import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from page.shop_object import ShopObject

@allure.title("Проверка итоговой стоимости товаров")
@allure.description("Данный тест проверяет общую стоимость выбранных товаров")
@allure.feature("READ")
@allure.severity("critical")
def test_shop():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    shop_object = ShopObject(browser)
    with allure.step("Заполняем поля страницы авторизации"):
        shop_object.start_page("standard_user", "secret_sauce")
    with allure.step("Добавляем товары в корзину"):
        shop_object.main_page()
    with allure.step("Подтверждаем карту"):
        shop_object.cart()
    with allure.step("Заполняем данные анкеты"):
        shop_object.checkout("Сергей", "Сибиряков", "669090")
    with allure.step("Выводим итоговую стоимость"):
        shop_object.total()

    with allure.step("Проверяем итоговую стоимость"):
        assert shop_object.total() == "Total: $58.29"
