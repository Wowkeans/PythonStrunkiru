from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class Item642Page(Base):

    url = 'https://www.strunki.ru/catalog/electric_guitar_strings/ghs-coated-boomers-cb-gbl-10-13-17-26-36-46'

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    #Locators

    add_to_cart_button = '//button[@name="shk-submit"]'
    message_order_now = '//button[contains(text(), "закажу сейчас")]'
    cart_button = '//a[contains(@href, "cart.php") and text()="Корзина"]'
    go_to_cart_button = "ПЕРЕЙТИ В КОРЗИНУ"



    #Getters

    def get_add_to_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart_button)))

    def get_message_order_now(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.message_order_now)))

    def get_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_button)))

    def get_go_to_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.LINK_TEXT, self.go_to_cart_button)))



    #Action

    def click_add_to_cart_button(self):
        self.get_add_to_cart_button().click()
        print('Click Add to Cart')

    def click_message_order_now(self):
        self.get_message_order_now().click()
        print('Click Order Now')

    def click_cart_button(self):
        self.get_cart_button().click()
        print('Click Cart')

    def click_go_to_cart_button(self):
        self.get_go_to_cart_button().click()
        print('Click Go to Cart')


    #Methods

    def go_to_cart(self):
        self.get_current_url()
        self.click_add_to_cart_button()
        self.click_message_order_now()
        self.click_cart_button()
        self.click_go_to_cart_button()
        self.save_screenshot()

