from appium import webdriver
from time import sleep

def swipeUp(driver,t=500,n=1):
    '''向上滑动'''
    size = driver.get_window_size()
    x1 = size['width']*0.5 # x坐标
    y1 = size['height']*0.75 # y 起始坐标
    y2 = size['height']*0.25 # y 终点坐标
    for i in range(n):
        driver.swipe(x1,y1,x1,y2,t)

def swipeDown(driver,t=500,n=1):
    '''向下滑动'''
    size = driver.get_window_size()
    x1 = size['width']*0.5 # x坐标
    y1 = size['height']*0.25 # y起点坐标
    y2 = size['height']*0.75 # y终点坐标
    for i in range(n):
        driver.swipe(x1,y1,x1,y2,t)

def swipeLeft(driver,t=500,n=1):
    '''向左滑动'''
    size = driver.get_window_size()
    x1 = size['width']*0.75 # x起始坐标
    x2 = size['width']*0.05 # x终点坐标
    y = size['height']*0.5 # y坐标
    for i in range(n):
        driver.swipe(x1,y,x2,y,t)

def swipeRight(driver,t=500,n=1):
    '''向右滑动'''
    size = driver.get_window_size()
    x1 = size['width']*0.05 # x起始坐标
    x2 = size['width']*0.75 # x终点坐标
    y = size['height']*0.5 # y坐标
    for i in range(n):
        driver.swipe(x1,y,x2,y,t)