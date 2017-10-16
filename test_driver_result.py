#!/usr/bin/env python
# -*- coding:utf-8 -*-

from selenium import webdriver

driver = webdriver.Firefox()
driver.get('http://www.baidu.com')

print('before test')
title = driver.title
print(title)
now_url = driver.current_url
print(now_url)

driver.find_element_by_id('kw').send_keys('selenium')
driver.find_element_by_id('su').click()

print('after test')
title1 = driver.title
print(title1)
now_url_1 = driver.current_url
print(now_url_1)

text = driver.find_elements_by_xpath(".//*[@id='container']/div[2]/div/div[2]")[0].text
print(text)

driver.quit()



