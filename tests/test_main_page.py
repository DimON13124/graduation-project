import allure
import pytest_check as check
from locators.maine_page import MainPage


@allure.story('Тест для проверки главной страницы')
@allure.feature('Тест для проверки хедера')
def test_maine_headers(web_browser):
    """Этот тест проверяет хедэр главной страницы"""

    locators = MainPage(web_browser)

    header_elements = [
        (locators.btn_contacts, "Контакты"),
        (locators.btn_services_to_passengers, "Услуги пассажирам"),
        (locators.btn_freight_transportation, "Грузовые перевозки"),
        (locators.btn_tourism_and_rest, "Туризм и отдых"),
        (locators.btn_corporate, "Корпаротивный"),
        (locators.btn_press_center, "Пресс-центр")
    ]

    for elements, elements_text in header_elements:
        check.is_true(elements.is_visible())
        check.is_true(elements.is_clickable())
        check.equal(elements.get_text(), elements_text)
