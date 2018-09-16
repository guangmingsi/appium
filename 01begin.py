import os
import unittest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time
import public.BaseAction
from public.InitSession import InitSession


#Appium环境配置
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__),p)
)

class AppTest(unittest.TestCase):
    def setUp(self):
        self.caps = InitSession('Android','4.4.2','noxx','com.baidu.searchbox',
                                'com.baidu.searchbox.SplashActivity')
        print(1)
        self.driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', self.caps.desired_caps)
        print('initscesss')
    def tearDown(self):
        self.driver.quit()
        pass
    def test_bdApp(self):
        self.driver.implicitly_wait(20)
        self.driver.find_element_by_id('com.baidu.searchbox:id/positive_button').click()
        self.driver.find_element_by_id('com.baidu.searchbox:id/update_close').click()
        self.driver.find_element_by_id('com.baidu.searchbox:id/baidu_searchbox').send_keys(u'王倩')
        ele1=self.driver.find_element_by_xpath('.//*[@text="百度一下"]')
        ele1.click()
        self.driver.background_app(3)
        self.driver.back()
        print('back')
        public.BaseAction.swipeDown(self.driver)
        public.BaseAction.swipeUp(self.driver)
        #self.driver.forward()
        #print('forward')


if __name__ == '__main__':
    suite = unittest.TestSuite()
    unittest.main()


