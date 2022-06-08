from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_BUTTON = (By.CSS_SELECTOR, "a.btn.btn-default[href$='/basket/']")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_FIRST_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_SECOND_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")


class ProductPageLocators:
    BUTTON_ADD_TO_CARD = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.col-sm-6>h1")
    MESSAGE_ABOUT_ADDING_PRODUCT = (By.CSS_SELECTOR, "div .alertinner>strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.col-sm-6>p.price_color")
    TOTAL_PRICE = (By.CSS_SELECTOR, "div.alertinner>p strong")


class BasketPageLocators:
    BASKET_IS_EMPTY = (By.CSS_SELECTOR, "#content_inner>p")
    THERE_ARE_ITEMS_IN_THE_BASKET = (By.CSS_SELECTOR, ".basket-items")