from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class CartPage(Base):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    #Locators

    full_name = '//input[@name="fullname"]'
    phone_number = '//input[@name="phone"]'
    address = '//input[@name="address"]'
    choose_shop_button = '//span[@class="title" and text()="STRUNKI.RU магазин"]/../a[@class="pvz-id"]'
    choose_pvz_1 = '//a[@data-address="443099, Самара, ул. Галактионовская, д.30"]'
    payment_method = "payment_receipt"
    clear_cart_button = '//a[contains(text(), "Очистить") and contains(@class, "cart-action")]'
    yes_button = '//button[text()="Да"]'

    #Getters

    def get_full_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.full_name)))

    def get_phone_number(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.phone_number)))

    def get_address(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.address)))

    def get_clear_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.clear_cart_button)))

    def get_yes_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.yes_button)))

    #Action

    def input_full_name(self, full_name):
        self.get_full_name().send_keys(full_name)
        print('Input Full Name')

    def input_phone_number(self, phone_number):
        self.get_phone_number().clear()
        self.get_phone_number().send_keys(phone_number)
        print('Input Phone Number')

    def input_address(self, address):
        self.get_address().clear()
        self.get_address().send_keys(address)
        print('Input Address')

    def click_clear_cart_button(self):
        self.get_clear_cart_button().click()
        print('Click Clear Cart Button')
        self.get_yes_button().click()
        print('Click Yes Button')



    #Methods

    def product_confirmation(self):
        self.get_current_url()
        self.input_full_name('Иванов Иван Иванович')
        self.input_phone_number('9200000000')
        self.input_address('г Москва, Красная Площадь д1')
        self.save_screenshot()



