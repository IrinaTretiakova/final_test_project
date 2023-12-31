import pytest
#import conftest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.support.ui import WebDriverWait
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.base_page import BasePage

link = "http://selenium1py.pythonanywhere.com/"


@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser): 
        #link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page() 
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()

# def test_guest_should_see_register_form(browser):
#     page = MainPage(browser, link)
#     page.open()
#     page.go_to_login_page() 
#     login_page = LoginPage(browser, browser.current_url)
#     login_page.should_be_register_form()

# def test_guest_should_see_login_form(browser):
#     page = MainPage(browser, link)
#     page.open()
#     page.go_to_login_page() 
#     login_page = LoginPage(browser, browser.current_url)
#     login_page.should_be_login_form()

# def test_should_be_login_url(browser):
#     page = MainPage(browser, link)
#     page.open()
#     page.go_to_login_page() 
#     login_page = LoginPage(browser, browser.current_url)
#     login_page.should_be_login_url()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.basket_has_no_goods()
    basket_page.can_see_empty_basket_message()