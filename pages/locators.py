from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    REGISTR_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")

class ProductPageLocators():
    ADD_BASKET = (By.XPATH, ".btn-lg.btn-primary")
    PRODUCT_NAME = (By.XPATH, ".product_main>h1")
    PRODUCT_ADDED = (By.XPATH, "#messages>.alert-safe:nth-child(1)>.alertinner>strong")
    
    
