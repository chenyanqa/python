#!/usr/bin/env python
# -*- coding:utf-8 -*-

from selenium import webdriver

driver = webdriver.Firefox()
driver.get('http://www.youdao.com')

cookie = driver.get_cookies()

for cookie in driver.get_cookies():
	print('%s->%s' % (cookie['name'],cookie['value']))

#print(cookie)

driver.quit()