#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time
from selenium import webdriver


driver = webdriver.Firefox()
'''
隐式等待时间 一旦设置则在webdriver实例周期中 都会起作用，则后续driver每查找一个元素
都会 先去DOM中去寻找元素，如果没有找到则等待一段时间，再去看下，如果超过设置的超时时间阈值
还没找到 则抛出异常
'''
driver.implicitly_wait(10)
driver.get('http://www.baidu.com')

#获取搜索主页的窗口句柄
search_windows = driver.current_window_handle
print(search_windows)
print(driver.title)

#driver.find_element_by_link_text('登录').click()  #不生效 sad
driver.find_element_by_xpath(".//*[@id='u1']/a[7]").click()
driver.find_element_by_link_text('立即注册').click()
#driver.find_element_by_xpath(".//*[@id='TANGRAM__PSP_10__submitWrapper']/a[1]").click()

#获取当前打开的所有窗口句柄
all_handles = driver.window_handles
print(all_handles)

#进入注册窗口
for handle in all_handles:
	if handle != search_windows:
		driver.switch_to.window(handle)
		print('now register window')
		driver.find_element_by_name('userName').send_keys('chenyan_123')
		driver.find_element_by_name('phone').send_keys('13641235237')
		#


driver.quit()







