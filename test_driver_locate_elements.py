#!/usr/bin/env python
# -*- coding:utf-8 -*-

from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get('http://www.baidu.com')

driver.find_element_by_id('kw').send_keys('selenium')
driver.find_element_by_id('su').click()
time.sleep(2)

'''
定位一组元素的xpath，可以先定位到某一个，例如“.//*[@id='8']/h3/a”，然后找到其父元素
即可.
'''
texts = driver.find_elements_by_xpath(".//div/h3/a")

for t in texts:
	print(t.text)

driver.quit()


