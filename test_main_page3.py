import pytest
#import conftest
from selenium import webdriver
from .pages.main_page import MainPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.support.ui import WebDriverWait

link = "http://selenium1py.pythonanywhere.com/"

def test_guest_can_go_to_login_page(browser): 
    #link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page() 

def test_guest_should_see_login_link(browser):
    #link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()