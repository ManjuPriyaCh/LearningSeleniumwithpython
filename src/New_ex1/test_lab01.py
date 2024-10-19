from selenium import webdriver
import allure
import pytest
import time
@allure.title("Verify the title of the webpage")
def test_sample():
    driver = webdriver.Chrome()
    driver.get("https://sdet.live")

def test_sample2():
    driver = webdriver.Edge()
    driver.get("https://test.cloudhealthtools.com/sign-in")
    time.sleep(8)



