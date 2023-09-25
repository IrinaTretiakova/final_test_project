from .base_page import BasePage
from .locators import MainPageLocators
from .login_page import LoginPage
from .locators import LoginPageLocators
from .locators import BasketPageLocators
from selenium.webdriver.common.by import By

class BasketPage(BasePage):
    def basket_has_no_goods(self):
        assert self.is_not_element_present(*BasketPageLocators.GOODS_PRESENCE), "There are goods in basket"

    def can_see_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), "There is no basket empty message"    