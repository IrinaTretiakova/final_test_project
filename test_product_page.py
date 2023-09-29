import pytest
#import conftest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.support.ui import WebDriverWait
from .pages.main_page import MainPage
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)

        email = str(time.time()) + "@fakemail.org"
        password = 102080307465
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, link)
        page.open()
        #page.should_be_added_in_basket()
        product_page = ProductPage(browser, browser.current_url)
        product_page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.should_be_added_in_basket()
        product_page = ProductPage(browser, browser.current_url)
        product_page.should_be_added_in_basket()    

@pytest.mark.need_review
@pytest.mark.skip
@pytest.mark.xfail
def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_added_in_basket()
    product_page = ProductPage(browser, browser.current_url)
    product_page.should_be_added_in_basket()
    product_page.should_not_be_success_message()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.basket_has_no_goods()
    basket_page.can_see_empty_basket_message()

def test_guest_can_see_added_message(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_added_in_basket()
    #page.should_be_added_message()
    product_page = ProductPage(browser, browser.current_url)
    product_page.should_be_added_message()

def test_guest_can_see_product_name_in_added_message(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_added_in_basket()
    #page.should_be_product_name_in_added_message()
    product_page = ProductPage(browser, browser.current_url)
    product_page.should_be_product_name_in_added_message()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.basket_has_no_goods()
    basket_page.can_see_empty_basket_message()