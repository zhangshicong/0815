from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(r'D:\Program Files\chromedriver.exe')

driver.implicitly_wait(10)

driver.get('https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc')

fstEle = driver.find_element_by_id('fromStationText')
fstEle.click()
fstEle.clear()
fstEle.send_keys('南京\n')

tstEle = driver.find_element_by_id('toStationText')
tstEle.click()
tstEle.clear()
tstEle.send_keys('郑州\n')

time = Select(driver.find_element_by_id('cc_start_time'))
time.select_by_visible_text('18:00--24:00')#可见内容查找

dr = driver.find_element_by_css_selector('#date_range li:nth-child(3)')
dr.click()

xpath = '//*[@id="queryLeftTable"]//td[4][@class]/../td[1]//a'
theXpath = driver.find_elements_by_xpath(xpath)
for one in theXpath:
    print(one.text)

driver.quit()

