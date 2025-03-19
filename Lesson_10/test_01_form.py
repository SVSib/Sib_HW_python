import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from page.form_object import FormObject


@allure.title("Проверка заполнения полей")
@allure.description("Заполненные поля окрашены в зеленый цвет, не заполненные поля окрашены в красный цвет")
@allure.feature("READ")
@allure.severity("normal")
def test_form():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    form_object = FormObject(browser)
    with allure.step("Заполняем поле 'Имя'"):
        form_object.first_name("Иван")

    with allure.step("Заполняем поле 'Фамилия'"):
        form_object.last_name("Петров")

    with allure.step("Заполняем поле 'Адрес'"):
        form_object.address("Ленина, 55-3")

    with allure.step("Заполняем поле 'Эмэил'"):
        form_object.e_mail("test@skypro.com")

    with allure.step("Заполняем поле 'Телефон'"):
        form_object.phone("+7985899998787")

    with allure.step("Не заполняем поле 'Zip-code'"):
        form_object.zip_code("")

    with allure.step("Заполняем поле 'Город'"):
        form_object.city("Москва")

    with allure.step("Заполняем поле 'Страна'"):
        form_object.country("Россия")

    with allure.step("Заполняем поле 'Должность'"):
        form_object.job_position("QA")

    with allure.step("Заполняем поле 'Компания'"):
        form_object.company("SkyPro")

    with allure.step("Задаем цвета полей для сравнения"):
        red = "rgba(132, 32, 41, 1)"
        green = "rgba(15, 81, 50, 1)"

    with allure.step("Проверяем цвет поля 'zip-code'"):
        assert form_object.set_color("zip-code") == red

    with allure.step("Проверяем цвет поля 'Имя'"):
        assert form_object.set_color("first-name") == green

    with allure.step("Проверяем цвет поля 'Фамилия'"):
        assert form_object.set_color("last-name") == green

    with allure.step("Проверяем цвет поля 'Адрес'"):
        assert form_object.set_color("address") == green

    with allure.step("Проверяем цвет поля 'эмэил'"):
        assert form_object.set_color("e-mail") == green

    with allure.step("Проверяем цвет поля 'Телефон'"):
        assert form_object.set_color("phone") == green

    with allure.step("Проверяем цвет поля 'Город'"):
        assert form_object.set_color("city") == green

    with allure.step("Проверяем цвет поля 'Страна'"):
        assert form_object.set_color("country") == green

    with allure.step("Проверяем цвет поля 'Должность'"):
        assert form_object.set_color("job-position") == green

    with allure.step("Проверяем цвет поля 'Компания'"):
        assert form_object.set_color("company") == green
