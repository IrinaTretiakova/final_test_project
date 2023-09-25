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

#link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"



# @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                #   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                #   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                #   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                #   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                #   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                #   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                #   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                #   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                #   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
# def test_guest_can_add_product_to_basket(browser):
#     ## link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_be_added_in_basket()
#     product_page = ProductPage(browser, browser.current_url)
#     product_page.should_be_added_in_basket()
#     product_page.should_not_be_success_message()
#     ## product_page.should_be_added_message()
#     ## product_page.should_be_product_name_in_added_message()

# def test_message_disappeared_after_adding_product_to_basket(browser):
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_be_added_in_basket()
#     product_page = ProductPage(browser, browser.current_url)
#     product_page.should_be_added_in_basket()
#     product_page.should_dissapear_of_success_message()

# def test_guest_should_see_login_link_on_product_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_be_login_link()

# def test_guest_can_go_to_login_page_from_product_page(browser):
#     page = ProductPage(browser, link)
#     page.open()
#     page.go_to_login_page()

# def test_guest_can_see_added_message(browser):
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_be_added_in_basket()
#     #page.should_be_added_message()
#     product_page = ProductPage(browser, browser.current_url)
#     product_page.should_be_added_message()

# def test_guest_can_see_product_name_in_added_message(browser):
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_be_added_in_basket()
#     #page.should_be_product_name_in_added_message()
#     product_page = ProductPage(browser, browser.current_url)
#     product_page.should_be_product_name_in_added_message()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.basket_has_no_goods()
    basket_page.can_see_empty_basket_message()