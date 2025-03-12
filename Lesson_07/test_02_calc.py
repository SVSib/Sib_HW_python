from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from page.calc_object import CalcObject


def test_calc():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    calc_object = CalcObject(browser)
    calc_object.delay(10)
    calc_object.keyboard("7")
    calc_object.keyboard("+")
    calc_object.keyboard("8")
    calc_object.keyboard("=")

    assert calc_object.timer() == 10
    assert calc_object.result() == "15"
