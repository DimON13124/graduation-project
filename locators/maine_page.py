import os
from page.base_page import WebPage
from page.elements import WebElement
from termcolor import colored


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://www.rw.by/'

        super().__init__(web_driver, url)

    btn_all_site_header = WebElement(xpath='(//a[@class="site-map"])[2]')
    btn_contacts = WebElement(xpath='(//*[@id="main_menu"]//b)[1]')
    btn_services_to_passengers = WebElement(xpath='(//*[@id="main_menu"]//b)[2]')
    btn_freight_transportation = WebElement(xpath='(//*[@id="main_menu"]//b)[3]')
    btn_tourism_and_rest = WebElement(xpath='(//*[@id="main_menu"]//b)[4]')
    btn_corporate = WebElement(xpath='(//*[@id="main_menu"]//b)[5]')
    btn_press_center = WebElement(xpath='(//*[@id="main_menu"]//b)[6]')
