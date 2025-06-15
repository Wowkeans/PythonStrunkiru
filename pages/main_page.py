from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class MainPage(Base):

    url = 'https://www.strunki.ru/'

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    #Locators

    login_button = '//button[contains(@class, "login-btn")]'
    email = '//input[@name="username"]'
    password = '//input[@name="password"]'
    enter_button = '//button[@name="cmdweblogin"]'
    strings = '//a[.//span[text()="Струны"]]'
    strings_6 = '//a[text()="6-струнные" and contains(@href, "strings_electric_6")]'
    electronics = '//a[.//span[text()="Электроника"]]'
    jacks = '//a[text()="Джеки (jack)" and contains(@href, "electricparts__big_jack")]'
    amps_fx = '//a[.//span[text()="Усиление, эффекты"]]'
    guit_cabs = '//a[text()="Гитарные кабинеты" and contains(@href, "gitarnye-kabinety")]'

    #Getters

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_email(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.email)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_enter_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.enter_button)))

    def get_strings(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.strings)))

    def get_strings_6(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.strings_6)))

    def get_electronics(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.electronics)))

    def get_jacks(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.jacks)))

    def get_amps_fx(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.amps_fx)))

    def get_guit_cabs(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.guit_cabs)))


    #Action

    def click_login_button(self):
        self.get_login_button().click()
        print('Click Login Button')

    def input_email(self, email):
        self.get_email().send_keys(email)
        print('Input Email')

    def input_password(self, password):
        self.get_password().send_keys(password)
        print('Input Password')

    def click_enter_button(self):
        self.get_enter_button().click()
        print('Click Enter Button')

    def click_strings(self):
        self.get_strings().click()
        print('Click Strings')

    def click_strings_6(self):
        self.get_strings_6().click()
        print('Click 6 Strings')

    def click_electronics(self):
        self.get_electronics().click()
        print('Click Electronics')

    def click_jacks(self):
        self.get_jacks().click()
        print('Click Jacks')

    def click_amps_fx(self):
        self.get_amps_fx().click()
        print('Click Amp/FX')

    def click_guit_cabs(self):
        self.get_guit_cabs().click()
        print('Click Guitar Cabinets')

    #Methods

    def authorization(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_login_button()
        self.input_email('study86_watery@icloud.com')
        self.input_password('kopmiv-Dirruq-hygqe3')
        self.click_enter_button()

    def go_to_se6p(self):
        self.click_strings()
        self.click_strings_6()
        self.save_screenshot()

    def go_to_jacks(self):
        self.click_electronics()
        self.click_jacks()
        self.save_screenshot()

    def go_to_guit_cabs(self):
        self.click_amps_fx()
        self.click_guit_cabs()
        self.save_screenshot()
