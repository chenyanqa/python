#!/usr/bin/env python
# -*- coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get('http://www.baidu.com')

#设置鼠标悬停
#elem = driver.find_element_by_link_text('设置')  #这个定位元素方式经常会失效
elem = driver.find_element_by_xpath(".//*[@id='u1']/a[8]")
ActionChains(driver).move_to_element(elem).perform()
time.sleep(1)

#打开搜索设置
driver.find_element_by_link_text('搜索设置').click()
time.sleep(2)

#保持设置
driver.find_element_by_class_name('prefpanelgo').click()
time.sleep(2)

#alert框处理
print(driver.switch_to.alert.text)
#driver.switch_to.alert.send_keys('test') #由于该警告框不接受文案输入，该方法会报错
driver.switch_to.alert.accept()
#driver.switch_to.alert.dismiss()  #此处dismiss操作也会让对话框消失
time.sleep(3)
driver.quit()


