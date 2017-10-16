#!/usr/bin/env python
# -*- coding:utf-8 -*-

from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get('http://www.baidu.com')

driver.find_element_by_id('kw').send_keys('selenium')
driver.find_element_by_id('su').click()
time.sleep(2)

driver.get_screenshot_as_file(r"D:\\cy\screenshot_test.png")

driver.quit()

