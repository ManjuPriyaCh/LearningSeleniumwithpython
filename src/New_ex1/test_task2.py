#Create a Selenium Script to verify the title for
#Open the Page - https://katalon-demo-cura.herokuapp.com/
#Verify the current URL, current title
#In the page source add a assertion that “CURA Healthcare Service” exist in the page. driver.pageSource() - Strin

from selenium import webdriver
import allure
import pytest
import time

def test_open_katalon():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/" # To verify URL
    page_source_data = driver.page_source
    assert "CURA Healthcare Service" in page_source_data # to verify text in page
    time.sleep(5)
    #assert "We Care About Your Health" in page_source_data