from selenium import webdriver

d = webdriver.Chrome(r'D:\Program Files\chromedriver.exe')
d.get('http://www.maiziedu.com/')

d.maximize_window()

ele = d.find_element_by_xpath('/html/body/div[2]/div/div/div/div/a[2]')
ele.click()

userele = d.find_element_by_id('id_account_l')
userele.click()
userele.clear()
userele.send_keys('18339819268')

pwdele = d.find_element_by_id('id_password_l')
pwdele.click()
pwdele.clear()
pwdele.send_keys('zsc07042044')

loginele = d.find_element_by_id('login_btn')
loginele.click()

