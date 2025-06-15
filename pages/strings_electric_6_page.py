import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class StringsElectric6Page(Base):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    #Locators

    filter_min = "slider-tv1_min_d"
    filter_max = "slider-tv1_max_d"
    show_button = '//button[@name="__submit"]'
    factory = '//span[@class="title" and text()="Производитель"]'
    ghs_checkbox = '//span[@class="title" and text()="GHS"]'
    caliber = '//span[@class="title" and text()="Калибр"]'
    cal_10_46 = '//span[@class="title" and text()="10-46"]'
    item_642 = '//a[contains(@href, "ghs-coated-boomers")]'

    #Getters

    def get_filter_min(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.ID, self.filter_min)))

    def get_filter_max(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.ID, self.filter_max)))

    def get_show_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.show_button)))

    def get_factory(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.factory)))

    def get_ghs_checkbox(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.ghs_checkbox)))

    def get_caliber(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.caliber)))

    def get_cal_10_46(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cal_10_46)))

    def get_item_642(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.item_642)))

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

    def click_ghs_checkbox(self):
        self.get_ghs_checkbox().click()
        print('Click GHS Checkbox')

    def click_caliber(self):
        self.get_caliber().click()
        print('Click Caliber')

    def click_cal_10_46(self):
        self.get_cal_10_46().click()
        print('Click 10-46 Checkbox')

    def click_item_642(self):
        self.get_item_642().click()
        print('Click Item 642')


    #Methods

    def buy_item_642(self):
        self.get_current_url()
        self.input_filter_min('2000')
        self.input_filter_max('3000')
        time.sleep(1)
        self.click_show_button()
        self.click_factory()
        self.driver.execute_script('window.scrollTo(0,100)')
        self.click_ghs_checkbox()
        self.click_caliber()
        self.click_cal_10_46()
        self.click_show_button()
        self.click_item_642()
        self.save_screenshot()


