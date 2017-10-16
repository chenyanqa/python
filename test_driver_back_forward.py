#!/usr/bin/env python
# -*- coding:utf-8 -*-

from selenium import webdriver
import time

#访问百度首页
driver = webdriver.Firefox()

#driver.get('http://baidu.com')

first_url = 'http://baidu.com'
print("now access is %s" %(first_url))
driver.get(first_url)

#访问新闻页面
#driver.get('http://news.baidu.com')

second_url = 'http://news.baidu.com'
print("now access is %s" %(second_url))
driver.get(second_url)

#返回到上一页
driver.back()
time.sleep(5)

#前进到新闻页
driver.forward()

time.sleep(10)
driver.quit()


