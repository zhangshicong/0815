from selenium import webdriver
from selenium.webdriver.support.ui import Select

d = webdriver.Chrome(r'D:\Program Files\chromedriver.exe')

d.get('https://www.baidu.com/')

ele = d.find_element_by_id('kw')
ele.click()
ele.clear()
ele.send_keys('51cto学院')

ele1 = d.find_element_by_id('su')
ele1.click()

d.implicitly_wait(10)

ele2 = d.find_element_by_xpath('//*[@id="1"]/h3/a[1]')
ele2.click()
d.maximize_window()
#d.implicitly_wait(30)

ele3 = d.find_element_by_css_selector('body > div:nth-child(9) > div:nth-child(1) > div > div.Login.tc > div.Btns > a:nth-child(1)')
ele3.click()#找不到元素

ele4 = d.find_element_by_link_text('账号密码登录')
ele4.click()

logele = d.find_element_by_id('loginform-username')
logele.click()
logele.clear()
logele.send_keys('18339819268')

pawele = d.find_element_by_id('loginform-password')
pawele.click()
pawele.clear()
pawele.send_keys('ZSC0704')

ele5 = d.find_element_by_xpath('//*[@id="login-form"]/div[3]/input[1]')
ele5.click()
pass
