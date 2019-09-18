from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import  ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select



def get_ele_time(driver, time, func):
    return WebDriverWait(driver, time).until(func)

def openBrower():
    webdriver_handle = webdriver.Chrome(r'D:\Program Files\chromedriver.exe')
    return webdriver_handle

def openUrl(handle, url):
    handle.get(url)

def findElement(d, arg):
    if 'text_id' in arg:
        ele_login = get_ele_time(d,10,lambda d:d.find_element_by_link_text(arg['text_id']))
        ele_login.click()
    useEle = d.find_element_by_id(arg['userid'])
    pwdEle = d.find_element_by_id(arg['pwdid'])
    loginEle = d.find_element_by_id(arg['loginid'])
    return useEle, pwdEle,loginEle

def sendVals(ele_tuple, arg, eletuple=None):
    listkey = ['unaem','pwd']
    i = 0
    for key in listkey:
        eletuple[i].send_keys('')
        eletuple[i].clean()
        eletuple[i].send_key(arg[key])
        i+=1
    ele_tuple[2].click()

def checkResult(d, text):
    try:
        d.find_element_by_link_text(text)
        print('Account And Pwd Error!')
    except:
        print('Account And Pwd Right!')

def login_test(ele_dict):
    d = openBrower()
    openUrl(d, ele_dict['Url'])
    d.maximize_window()
    ele_tuple = findElement(d, ele_dict)
    sendVals(ele_tuple, account_dict)
    checkResult(d,ele_dict['errorid'])


if __name__ =='__main__':
    url = 'http://www.maiziedu.com/'
    login_text = '登录'
    account = '18339819268'
    pwd = 'zsc07042044'
    ele_dict = {'Url':url,'text_id': login_text, 'userid': 'id_account_1', \
                'pwdid': 'id_password_l', 'loginid': 'login_btn',\
                'uname':account,'pwd':pwd,'errorid':'该账号格式不正确'}
    account_dict = {'uname': account, 'pwd': pwd}

    login_test(ele_dict)


