# coding = utf-8
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#创建一个浏览器实例
driver = webdriver.Firefox()
#通过浏览器的get函数访问url
driver.get('http://baidu.com')
#driver.set_window_size(480,800)
#driver.maximize_window()

#通过研究百度首页源码，发现搜索框input的id 为“kw”
#通过find_element_by_id（）来找到搜索框，并赋给elem
elem = driver.find_element_by_id("kw")
#向搜索框发送关键字
elem.send_keys("selenium")
#模拟键盘的Enter键提交
elem.send_keys(Keys.RETURN)

print(driver.title)  #这个print 是用来打印在py控制台的
time.sleep(15)
driver.quit()

