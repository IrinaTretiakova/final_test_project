from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    REGISTR_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")

class ProductPageLocators():
    ADD_BASKET = (By.XPATH, ".btn-lg.btn-primary")
    PRODUCT_NAME = (By.XPATH, "//*[@id='content_inner']/article/div[1]/div[2]/h1")
    # PRODUCT_ADDED = (By.XPATH, "//*[@id='messages']/div[1]/div/strong")
    SUCCESS_MESSAGE = (By.XPATH, "//*[@id='messages']/div[1]/div/strong")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET = (By.XPATH, '//span[@class="btn-group"]/a[1]')

class BasketPageLocators():
    GOODS_PRESENCE = (By.CSS_SELECTOR, ".col-sm-6.h3")
    EMPTY_BASKET_MESSAGE = (By.XPATH, '//div[@id="content_inner"]/p[1]')