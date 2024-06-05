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

@allure.story('Тест для проверки главной страницы')
@allure.feature('Тест для проверки адреса ссылок')
def test_headers_link(web_browser):
    "Этот тест проверяет адреса ссылок хедера главной страницы"


    locators = MainPage(web_browser)

    link_header_elements = [
        (locators.btn_home_link, 'https://www.rw.by/'),
        (locators.btn_contacts_link, 'https://www.rw.by/corporate/contacts/'),
        (locators.btn_services_to_passengers, 'https://pass.rw.by/ru/'),
        (locators.btn_freight_transportation, 'https://www.rw.by/cargo_transportation/'),
        (locators.btn_tourism_and_rest, 'https://www.rw.by/tourism_and_recreation/'),
        (locators.btn_corporate, 'https://www.rw.by/corporate/'),
        (locators.btn_press_center, 'https://www.rw.by/corporate/press_center/')
    ]

    with allure.step('Проверка')

