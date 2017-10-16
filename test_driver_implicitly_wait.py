#!/usr/bin/env python
# -*- coding:utf-8 -*-

from selenium import webdriver
from selenium.common.exceptions import NoSuchAttributeException
from time import ctime


driver = webdriver.Firefox()
#设置隐式等待10秒
driver.implicitly_wait(10)
driver.get('http://www.baidu.com')

try:
	print(ctime())   #打印当前本地时间，格式类似：Sun Oct 15 10:43:25 2017
	driver.find_element_by_id('kw').send_keys('selenium')
except NoSuchAttributeException as e:
	print(e)
finally:
	print(ctime())
	driver.quit()

