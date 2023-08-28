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

link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"

def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_added_in_basket()
    product_page = ProductPage(browser, browser.current_url)
    product_page.should_be_added_in_basket

def test_guest_can_see_added_message(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_added_in_basket()
    product_page = ProductPage(browser, browser.current_url)
    product_page.should_be_added_message

def test_guest_can_see_product_name_in_added_message(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_added_in_basket()
    product_page = ProductPage(browser, browser.current_url)
    product_page.should_be_product_name_in_added_message
