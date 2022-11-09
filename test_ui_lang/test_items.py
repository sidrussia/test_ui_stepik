import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_button_add_to_cart (browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(5)
    x = browser.find_element(By.XPATH, "//form[@id='add_to_basket_form']/child::button")
    assert x is not None, "There is no button 'Add to basket' "