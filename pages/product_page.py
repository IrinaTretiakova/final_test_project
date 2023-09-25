import math
import time

from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.by import By

from .base_page import BasePage
from .locators import MainPageLocators
from .locators import ProductPageLocators
from .main_page import MainPage


class ProductPage(BasePage):
    def should_be_added_in_basket(self):
        add_button = self.browser.find_element(By.CSS_SELECTOR, ".add-to-basket")
        add_button.click()
        self.solve_quiz_and_get_code()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        print(x)
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    # def should_not_be_success_message(self):
    #     assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
    #     "Success message is presented, but should not be"

    # def should_dissapear_of_success_message(self):
    #     assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
    #     "Success message is presented, but should not be"
    
    # def should_be_added_message(self):
    #     assert self.is_element_present(*ProductPageLocators.PRODUCT_ADDED), "Product isn't added to basket" 
   
    # def should_be_product_name_in_added_message(self):
    #     product_name_el = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
    #     product_added_msg_el = self.browser.find_element(*ProductPageLocators.PRODUCT_ADDED)
    #     product_name_text = product_name_el.text
    #     product_added_text = product_added_msg_el.text
    #     print(product_added_text)
    #     print('!!!!!!!!!!!!!!!!!!!!!!!')
    #     assert product_added_text == product_name_text, "Text doesn't contain product name"

    
