#!/usr/bin/env python3.6
#-*-coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pyquery import PyQuery as pq
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

browser = webdriver.Chrome()
###如果网络有延迟，请求等待时间10秒，默认等待0秒
browser.implicitly_wait(10)
###cookie处理
# cookie = {'name':'larry','vaule':'123456'}
# browser.add_cookie(cookie)

##设置网页下载时长超时时间秒
browser.set_page_load_timeout(20)
###截取当前页面屏幕
###browser.save_screenshot('/tmp/meinv1.png')

browser.get('https://www.baidu.com')
elme = browser.find_element_by_name('wd')
elme.clear()
elme.send_keys('python')
#匹配到元素，发送字符，之后submit提交
elme.submit()
time.sleep(3)
browser.back()
time.sleep(1)
browser.forward()
time.sleep(1)
elme2 = browser.find_element_by_name('wd')
time.sleep(1)
elme2.clear()
elme2.send_keys("动漫",Keys.RETURN)
time.sleep(2)

##quit是退出浏览器，close是关闭浏览器当前的标签
# browser.quit()

##向下滚动，翻页
n = 60
for i in range(1,n+1):
    s = "window.scrollTo(0,document.body.scrollHeight/{0}*{1});".format(n,i)
    browser.execute_script(s)
    time.sleep(0.1)

###判断name元素tj_login是否存在如果15秒内获取不到，执行except语句
try:
    elem3 = WebDriverWait(browser,15).until(
        # EC.presence_of_element_located((By.NAME,'tj_login'))
        EC.presence_of_element_located((By.CLASS_NAME,'n'))
    )

    elem3.click()
except:
    print('not find second page')
finally:
    time.sleep(2)
    # browser.quit()

###打开第二个浏览器窗口
##获取当前窗口handle,所有handle以及当前窗口title
cur_title = browser.title
cur_handle = browser.current_window_handle
all_handles = browser.window_handles
##构造一个地址,并执行访问之
js = "window.open('http://192.168.0.1')"
browser.execute_script(js)
time.sleep(2)
###根据handle切换到上一个窗口
browser.switch_to_window(cur_handle)



# doc = pq(browser.page_source)
# print(doc.text())
soup = BeautifulSoup(browser.page_source,'html.parser',from_encoding='utf-8')
# print(soup.text)

# ###登录
# login_tj = browser.find_element_by_name('tj_login1')
# ##click 上面匹配到元素，点击
# login_tj.click()
# user_login = browser.find_element_by_id('TANGRAM__PSP_10__footerULoginBtn')
# user_login.click()
# user_name = browser.find_element_by_name('userName')
# user_name.clear()
# user_name.send_keys('13718067768')
# time.sleep(3)
# password = browser.find_element_by_name('password')
# password.clear()
# password.send_keys('hello123')
# time.sleep(3)
# member_pass = browser.find_element_by_name('memberPass')
# member_pass.click()
# time.sleep(5)
# denglu = browser.find_element_by_xpath("//input[@id='TANGRAM__PSP_10__submit']")
# ##点击换验证码
# change_code = browser.find_element_by_id('TANGRAM__PSP_10__verifyCodeChange')
# change_code.click()
# time.sleep(2)
# change_code.click()
# time.sleep(2)
# denglu.submit()
