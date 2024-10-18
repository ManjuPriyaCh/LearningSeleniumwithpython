from selenium import webdriver

def test_open_vwo_login():
    driver = webdriver.Chrome()
    #Its generally a Post request which will create a fresh copy of chrome
    #Fresh-Chrome-sessionID

    driver.get("https://app.vwo.com")
    #code-->http request-chrome driver(Seleinum manager)-->Chrome (Sessionid)
    print(driver.title) #get request
    assert driver.title == "Login - VWO"

    #python interpreter will autimatically close the browser --Advantage*
