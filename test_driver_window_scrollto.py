#!/usr/bin/env python
# -*- coding:utf-8 -*-

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get('http://www.baidu.com')

driver.set_window_size(500, 500)

driver.find_element_by_id('kw').send_keys('selenium')
driver.find_element_by_id('kw').send_keys(Keys.ENTER)
#driver.find_element_by_id('su').click()

time.sleep(3)

#由于浏览器进度条操作selenium 没有提供对应的方法 因此需要借助js来完成
js = "window.scrollTo(100,450);"
driver.execute_script(js)
time.sleep(3)

driver.quit()
