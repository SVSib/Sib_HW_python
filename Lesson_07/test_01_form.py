from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from page.form_object import FormObject


def test_form():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    form_object = FormObject(browser)
    form_object.first_name("Иван")
    form_object.last_name("Петров")
    form_object.address("Ленина, 55-3")
    form_object.e_mail("test@skypro.com")
    form_object.phone("+7985899998787")
    form_object.zip_code("")
    form_object.city("Москва")
    form_object.country("Россия")
    form_object.job_position("QA")
    form_object.company("SkyPro")

    red = "rgba(132, 32, 41, 1)"
    green = "rgba(15, 81, 50, 1)"

    assert form_object.color_red("zip-code") == red
    assert form_object.color_green("first-name") == green
    assert form_object.color_green("last-name") == green
    assert form_object.color_green("address") == green
    assert form_object.color_green("e-mail") == green
    assert form_object.color_green("phone") == green
    assert form_object.color_green("city") == green
    assert form_object.color_green("country") == green
    assert form_object.color_green("job-position") == green
    assert form_object.color_green("company") == green
