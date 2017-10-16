#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

driver.get('http://baidu.com')

elem = driver.find_element_by_id('kw')
elem.send_keys('美丽说') #模拟键盘输入
elem.send_keys(Keys.RETURN) # Keys.RETURN与Keys.ENTER功效类似
time.sleep(2)

elem.clear()
# search_text = elem.send_keys('selenium')
# search_text.submit()

elem.send_keys('selenium')
elem1 = driver.find_element_by_id('su')
elem1.click()


time.sleep(5)
driver.quit()






