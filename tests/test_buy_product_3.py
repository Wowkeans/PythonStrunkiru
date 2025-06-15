import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.cart_page import CartPage
from pages.guit_cabs_page import GuitCabsPage
from pages.main_page import MainPage


def test_buy_product_642():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(options=chrome_options)

    mp = MainPage(driver)
    mp.authorization()
    mp.go_to_guit_cabs()

    gcp = GuitCabsPage(driver)
    gcp.buy_item_44565()

    cp = CartPage(driver)
    cp.product_confirmation()
    cp.click_clear_cart_button()

    time.sleep(2)


    driver.quit()
