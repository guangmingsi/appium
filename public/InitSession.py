class InitSession(object):
    def __init__(self,osName,osVersion,deviceName,packageName,appActivity,appDirection=''):
        self.desired_caps={}
        self.desired_caps['platformName'] = osName
        self.desired_caps['platformVersion'] = osVersion
        self.desired_caps['deviceName'] = deviceName
        self.desired_caps['app'] = appDirection
        #self.caps['appPackage'] = 'com.baidu.searchbox'
        self.desired_caps['appPackage'] = packageName
        #self.caps['appActivity'] = 'com.baidu.searchbox.SplashActivity'
        self.desired_caps['appActivity'] = appActivity
        self.desired_caps['unicodeKeyboard']='True'
        self.desired_caps['resetKeyboard'] = 'True'
