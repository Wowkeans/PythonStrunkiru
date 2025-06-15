import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.cart_page import CartPage
from pages.jacks_page import JacksPage
from pages.main_page import MainPage


def test_buy_product_18025():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(options=chrome_options)

    mp = MainPage(driver)
    mp.authorization()
    mp.go_to_jacks()

    jp = JacksPage(driver)
    jp.buy_item_18025()

    cp = CartPage(driver)
    cp.product_confirmation()
    cp.click_clear_cart_button()

    time.sleep(2)


    driver.quit()
