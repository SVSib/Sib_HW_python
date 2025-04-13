import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from page.calc_object import CalcObject


@allure.title("Проверка времени задержки и результата вычислений")
@allure.description("Данный тест проверяет установленное время задержки и конечный результат вычислений")
@allure.feature("READ")
@allure.severity("critical")
def test_calc():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    calc_object = CalcObject(browser)

    with allure.step("устанавливаем время задержки"):
        calc_object.delay(10)

    with allure.step("нажимаем кнопку '7'"):
        calc_object.keyboard("7")

    with allure.step("нажимаем кнопку '+'"):
        calc_object.keyboard("+")

    with allure.step("нажимаем кнопку '8'"):
        calc_object.keyboard("8")

    with allure.step("нажимаем кнопку '='"):
        calc_object.keyboard("=")

    with allure.step("проверяем время задержки"):
        assert calc_object.timer() == 10

    with allure.step("проверяем полученный результат"):
        assert calc_object.result() == "15"
