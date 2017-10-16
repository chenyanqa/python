#!/usr/bin/env python
# -*- coding:utf-8 -*-

from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get('http://baidu.com')

elem = driver.find_element_by_xpath(".//*[@id='u1']/a[8]")
ActionChains(driver).move_to_element(elem).perform()
time.sleep(2)

driver.find_element_by_link_text('搜索设置').click()
time.sleep(2) #主要用于页面加载

sel = driver.find_element_by_id('nr')
#Select(sel).select_by_value('50')
Select(sel).select_by_index(2)
time.sleep(2)

driver.find_element_by_class_name('prefpanelgo').click()
time.sleep(2)

driver.switch_to.alert.accept()
time.sleep(2)

driver.quit()

