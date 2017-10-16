#!/usr/bin/env python
# -*- coding:utf-8 -*-

from selenium import webdriver

driver = webdriver.Firefox()
driver.get('http://baidu.com')

#获取百度首页搜索框大小
size = driver.find_element_by_id('kw').size
print(size)

#获取百度首页底部备案信息
text = driver.find_element_by_id('cp').text
print(text)

#获取元素的属性值，可以是id，name，type或其他任意属性

attribute = driver.find_elements_by_id('su')[0].get_attribute('value')
print(attribute)

#返回元素的结果是否可见
result = driver.find_element_by_id('kw').is_displayed()
print(result)

driver.quit()