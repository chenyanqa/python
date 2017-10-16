#!/usr/bin/env python
# -*- coding:utf-8 -*-

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get('http://www.baidu.com')

#输入内容selenium
elem = driver.find_element_by_id('kw')
elem.send_keys('selenium')
time.sleep(2)
#输入删除键，删除一个m
elem.send_keys(Keys.BACKSPACE)

time.sleep(2)
#输入一个空格键，但是没有生效。。。
elem.send_keys(Keys.SPACE)
time.sleep(2)
#输入教程
elem.send_keys('教程')
time.sleep(2)

#输入ctrl+a 全选内容
elem.send_keys(Keys.CONTROL,'a')
time.sleep(2)

#输入ctrl+x  剪切内容
elem.send_keys(Keys.CONTROL,'x')
time.sleep(2)

elem.send_keys('test')
time.sleep(2)

#输入ctrl+v  粘贴内容
elem.send_keys(Keys.CONTROL,'v')
time.sleep(2)

# elem.send_keys(Keys.ENTER)
# time.sleep(2)

driver.find_element_by_id('su').click()
driver.quit()




