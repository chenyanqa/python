#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time
from selenium import webdriver

driver = webdriver.Firefox()
driver.get('http://www.126.com')
'''
有时候我们定位不到元素还有其它的原因，下面说明几种：
1.Frame/Iframe原因定位不到元素：
2.Xpath描述错误原因：
解决办法：编写好Xpath路径，chrome的F12->html，ctrl+F进行查找，看是否能查找到。
3.页面还没有加载出来，就对页面上的元素进行的操作：
解决办法：导入time模块设置等待时间。
4.动态id定位不到元素
解决办法：如果是动态的id，最好不要使用，转而使用xpath或其它方式定位
5.二次定位，如弹出框登录
解决办法：先定位到弹出框，再定位到弹出框内的元素。
6.不可见元素定位
[emoji:00a0] [emoji:00a0] [emoji:00a0]如上百度登录代码，通过名称为tj_login查找的登录元素，
有些是不可见的，所以加一个循环判断，找到可见元素（is_displayed()）点击登录即可。

'''
#126邮箱这个页面元素较多加载时间比较久，很可能出现页面没加载就开始操作导致定位不到元素的情况
time.sleep(5)
driver.switch_to.frame('x-URS-iframe')
driver.find_element_by_name('email').clear()
driver.find_element_by_name('email').send_keys('chen2987me')

driver.find_element_by_name('password').clear()
driver.find_element_by_name('password').send_keys('chen_2987')
driver.find_element_by_id('dologin').click()

time.sleep(1)
driver.find_element_by_link_text('继续登录').click()

driver.switch_to.default_content()

time.sleep(10)
driver.quit()