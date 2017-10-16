#!/usr/bin/env python
# -*- coding:utf-8 -*-

from selenium import webdriver

driver = webdriver.Firefox()
driver.get('http://www.youdao.com')

#向cookie的name、value中添加会话信息
driver.add_cookie({'name': 'key-aaaaaa', 'value': 'value-bbbbbb'})

driver.delete_cookie('___rl__test__cookies') #这个cookie的name 为 name键的值
#driver.delete_all_cookies()

#遍历cookies中的name、value 信息并打印 当然还有上面添加的信息
for cookie in driver.get_cookies():
	print('%s->%s' % (cookie['name'],cookie['value']))

driver.quit()



