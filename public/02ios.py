from appium import webdriver

cap ={
    'platformName': 'ios',
    'platformVersion': '11.4',
    'deviceName': 'iPhone X',
    'browserName': 'safari'
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',cap)
driver.get('https://m.baidu.com')