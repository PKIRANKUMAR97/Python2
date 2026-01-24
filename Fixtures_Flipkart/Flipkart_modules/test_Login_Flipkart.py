
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from confest import setup,driver

class TestLoginFlipkart:
    def test_LoginByEmailFlipkart(self, setup):
        print("test for Login by Email ")
        assert "Online Shopping India Mobile, Cameras, Lifestyle & more Online @ Flipkart.com" == driver.title

    def test_addtocart(self, setup):
        driver.find_element(By.XPATH,"//span[text()='Electronics']").click()
        driver.find_element(By.XPATH,"//a[text()='Cameras & Accessories']").click()
        driver.find_element(By.XPATH,"//a[text()='DSLR & Mirrorless']").click()
        driver.find_element(By.XPATH,"//div[normalize-space()='Canon EOS R50 V Mirrorless Camera Body withRF-S14-30mm F4-6.3IS STMPZ Lens']").click()
        # driver.find_element(By.XPATH,"//button[normalize-space()='Add to cart' & @class='dSM5Ub ugg2XR IUmgrZ']").click()

        driver.implicitly_wait(5)



