#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 设置元素显示等待

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get('http://www.baidu.com')
'''
1、元素显示等待的意思：就是必须等待某个条件成立时才继续执行，否则达到最大超时时间时抛出异常
2、WebDriverWait(driver, timeout, poll_frequency=0.5, ignored_exceptions=None)
3、WebDriverWait()一般由until()或until_not()方法配合使用， * until(method, message=‘’)
调用该方法提供的驱动程序作为一个参数，直到返回值为True
4、相关文档参考 http://www.jb51.net/article/92672.htm
5、http://www.cnblogs.com/yuuwee/p/6635652.html
'''
locator = (By.ID, 'kw')  #需要定位的内容
element = WebDriverWait(driver, 5, 0.5).until(EC.presence_of_element_located(locator))
try:
	element.send_keys('selenium')
except Exception:
	print(Exception)

# finally: 每次如果有finally 模块的话  程序会优先 将浏览器关掉，而不去执行 try中的内容。。
# 	print('haha')
# 	driver.quit()



# driver = webdriver.Firefox()
# driver.get("http://www.baidu.com")
# try:
#     element = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, "kw"))
#     )
# finally:
#     driver.quit()



