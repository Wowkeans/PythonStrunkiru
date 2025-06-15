import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class JacksPage(Base):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    #Locators

    filter_min = "slider-tv1_min_d"
    filter_max = "slider-tv1_max_d"
    show_button = '//button[@name="__submit"]'
    factory = '//span[@class="title" and text()="Производитель"]'
    canare = '//span[@class="title" and text()="Canare"]'
    add_item_18025 = 'button.shk-but-vk.btn-primary'
    cart_button = '//a[contains(@href, "cart.php") and text()="Корзина"]'
    go_to_cart_button = "ПЕРЕЙТИ В КОРЗИНУ"

    #Getters

    def get_filter_min(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.ID, self.filter_min)))

    def get_filter_max(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.ID, self.filter_max)))

    def get_show_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.show_button)))

    def get_factory(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.factory)))

    def get_canare(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.canare)))

    def get_add_item_18025(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.add_item_18025)))

    def get_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_button)))

    def get_go_to_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.LINK_TEXT, self.go_to_cart_button)))

    #Action

    def input_filter_min(self, filter_min):
        self.get_filter_min().clear()
        self.get_filter_min().send_keys(filter_min)
        print('Input Filter Min')

    def input_filter_max(self, filter_max):
        self.get_filter_max().clear()
        self.get_filter_max().send_keys(filter_max)
        print('Input Filter Max')

    def click_show_button(self):
        self.get_show_button().click()
        print('Click Show Button')

    def click_factory(self):
        self.get_factory().click()
        print('Click Factory')

    def click_canare(self):
        self.get_canare().click()
        print('Click Canare Checkbox')

    def click_add_item_18025(self):
        self.get_add_item_18025().click()
        print('Add Item 18025')

    def click_cart_button(self):
        self.get_cart_button().click()
        print('Click Cart')

    def click_go_to_cart_button(self):
        self.get_go_to_cart_button().click()
        print('Click Go to Cart')


    #Methods

    def buy_item_18025(self):
        self.get_current_url()
        self.input_filter_min('500')
        time.sleep(1)
        self.input_filter_max('700')
        time.sleep(1)
        self.click_show_button()
        self.click_factory()
        self.click_canare()
        self.click_show_button()
        time.sleep(1)
        self.driver.execute_script('window.scrollTo(0,100)')
        self.click_add_item_18025()
        self.click_cart_button()
        self.click_go_to_cart_button()
        self.save_screenshot()


