#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time
from selenium import webdriver

# driver = webdriver.Firefox()
# driver.implicitly_wait(10)
#
# driver.get('http://www.126.com')
# time.sleep(3)
#
# driver.switch_to.frame('x-URS-iframe')
# driver.find_element_by_name('email').clear()
# driver.find_element_by_name('email').send_keys('chen2987me')
#
# driver.find_element_by_name('password').clear()
# driver.find_element_by_name('password').send_keys('chen_2987')
# driver.find_element_by_id('dologin').click()
# time.sleep(1)
#
# driver.find_element_by_link_text('继续登录').click()
# driver.switch_to.default_content()
#
# time.sleep(5)
#
# #点击写信按钮
# driver.find_element_by_xpath(".//*[@id='_mail_component_70_70']").click()
# time.sleep(5)
# #driver.find_element_by_xpath(".//*[@id='1508077913125_attachBrowser']/input").click()
# driver.find_element_by_class_name('O0').click()   #总定位不到 无解了。。。
#
# # time.sleep(10)
# # driver.quit()


#上传页面网址：http://www.sahitest.com/demo/php/fileUpload.htm
driver = webdriver.Firefox()
driver.get('http://www.sahitest.com/demo/php/fileUpload.htm')

upload = driver.find_element_by_id('file')
upload.send_keys(r'D:\\cy\tt.py')
print(upload.get_attribute('value'))




