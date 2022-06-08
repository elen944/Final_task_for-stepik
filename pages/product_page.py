from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def click_add_to_cart_button(self):
        add_to_cart = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_CARD)
        add_to_cart.click()

    def should_be_message_about_adding(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message_about_adding_product = self.browser.find_element(*ProductPageLocators.MESSAGE_ABOUT_ADDING_PRODUCT).text
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME),\
            "Couldn`t found PRODUCT NAME"
        assert self.is_element_present(*ProductPageLocators.MESSAGE_ABOUT_ADDING_PRODUCT),\
            "Couldn`t found MESSAGE ABOUT ADDING"
        assert product_name == message_about_adding_product,\
            f"PRODUCT NAME='{product_name}' MESSAGE ='{message_about_adding_product}'"

    def should_be_total_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        total_price_on_product_page = self.browser.find_element(*ProductPageLocators.TOTAL_PRICE).text
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE),\
            "Couldn`t found PRODUCT PRICE"
        assert self.is_element_present(*ProductPageLocators.TOTAL_PRICE),\
            "Couldn`t found TOTAL PRICE"
        assert product_price == total_price_on_product_page,\
            f"PRODUCT PRICE='{product_price}' TOTAL PRICE ='{total_price_on_product_page}'"

    def should_not_be_message_about_adding(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_ABOUT_ADDING_PRODUCT), \
            "Message about adding was presented, shouldn`t be"

    def should_disappeared_message_about_adding(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_ABOUT_ADDING_PRODUCT), \
            "Message about adding was`t disappeared"