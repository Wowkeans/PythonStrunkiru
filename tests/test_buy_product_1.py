import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from pages.cart_page import CartPage

from pages.item_642_page import Item642Page

from pages.main_page import MainPage
from pages.strings_electric_6_page import StringsElectric6Page


# @pytest.mark.order(3)
def test_buy_product_642():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(options=chrome_options)

    mp = MainPage(driver)
    mp.authorization()
    mp.go_to_se6p()


    se6p = StringsElectric6Page(driver)
    se6p.buy_item_642()

    i642p = Item642Page(driver)
    i642p.go_to_cart()

    cp = CartPage(driver)
    cp.product_confirmation()
    cp.click_clear_cart_button()

    time.sleep(2)

    driver.quit()
