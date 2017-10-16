#!/usr/bin/env python
# -*- coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Firefox()
driver.get('http://baidu.com')
'''
此时如果通过 elem = driver.find_elements_by_('tj_settingicon')来定位元素的话
会报错，TypeError: 'method' object is not subscriptable，因为可以有鼠标悬浮
效果的一般都是超链接，因此需要使用by_link_text('')
'''

elem = driver.find_element_by_xpath(".//*[@id='u1']/a[8]")
ActionChains(driver).move_to_element(elem).perform()
time.sleep(5)
driver.quit()