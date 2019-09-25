"""
#1到100累加
sum = 0
for i in range(101):
    sum += i
print(sum)


#猜随机数
import random
x = random.randint(1,100)
count = 0
while True:
    count += 1
    num = int(input('请输入数字：'))
    if num > x:
        print('大了')
    elif num < x:
        print('小了')
    else:
        print('对了')
        break
print('总共猜了%d次' %count)
if count > 7:
    print('有点笨')


#九九乘法表
for i in range(1,10):
    for j in range(i,10):
        print('%d*%d=%d' %(i, j, i*j),end='\t')
    print()



#判断一个数是不是素数
from math import sqrt

num = int(input('请输入一个正整数：'))
end = int(sqrt(num))  #??为啥用end值
is_prime = True
for x in range(2, end+1):
    if num % x == 0:
        is_prime = False
        break
if is_prime and num != 1:
    print('%d是素数' %num)
else:
    print('%d不是素数' % num)



#输入两个正整数，计算最大公约数和最小公倍数。
a = int(input('请输入第一个值：'))
b = int(input('请输入第二个值：'))
if a > b:
    a, b = b, a
for factor in range(a, 0, -1):
    if a % factor ==0 and b % factor ==0:
        print('%d和%d的最大公约数是%d' %(a, b, factor))
        print('%d和%d的最小公倍数是%d' % (a, b, a*b//factor))  #这啥操作？？
        break



row = int(input('请输入行数：'))
for i in range(row):
    for _ in range(i+1):
        print('*', end = '')
    print()

row = int(input('请输入行数：'))
for i in range(row):
    for j in range(row):
        if j < row - i-1:
            print(' ', end='')
        else:
            print('*', end='')
    print()




#水仙花数
num = int(input('请输入三位正整数：'))
a = int(num / 100)
b = int(num / 10 - a*10)
c = int(num - a*100 - b*10)
print(a, b, c)

if a**3+b**3+c**3 == num:
    print('%d为水仙花数' %num)
else:
    print('%d不是水仙花数' %num)



#完全数
from math import sqrt
num = int(input('请输入正整数：'))
sum = 0
while True:
    for i in range(2, num):
        if num % i ==0:
           sum += i
    else:
        break
if sum+1 ==num:
    print('%d是完全数' %num )
else:
    print('%d不是完全数' %num)


#百鸡百钱
for num_cock in range(100):
    for num_hen in range(100):
        if 14*num_cock + 8*num_hen - 200 ==0 and\
            100 - num_hen - num_cock >= 0:
            print('公鸡有%d只，母鸡有%d只，小鸡%d只' %(num_cock, num_hen,(100-num_cock-num_hen)))


def foo():
    print('hello, world!')

def foo():
    print('goodbye, world!')

# 下面的代码会输出什么呢？
foo()#goodbye, world!


#最大公约数，最小公倍数，函数
def gcd(x, y):
    if x > y:
        (x, y) = (y, x)
    for factor in range(x, 0, -1):
        if x % factor ==0 and y % factor == 0:
            return factor

def lcm(x, y):
    return x * y // gcd(x, y)

x = int(input('x ='))
y = int(input('y ='))
print('最小公倍数为%d,最大公约数为%d' %(gcd(x, y),lcm(x, y)) )


#素数
def is_prime(num):
    for factor in range(2, num):
        if num % factor == 0:
            return False
    return True

num = int(input('num = '))
if is_prime(num) ==True:
    print('%d是素数' %num)
else:
    print('%d不是素数' % num)


s1 = r'\'hello, world!\''
s2 = r'\n\\hello, world!\\\n'
print(s1, s2, end='')       #r将符号都展示出来，包括换行符


#马灯
import os
import time
def main():
    content = '郑州轻工业大学欢迎你！！！'
    while True:
        os.system('cls')  #清除
        print(content)
        time.sleep(0.5)
        content = content[1:] + content[0]



#验证码
import random

def Verification_code(code_len = 4):
    all_char = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    stop_char = len(all_char) - 1
    code = ''
    for _ in range(code_len):
        index = random.randint(0, stop_char)
        code += all_char[index]
    return code

print(Verification_code())


#返回文件后缀名
def get_suffix(filename):
    point = filename.rfind('.')
    if 0 < point < len(filename):
        index = point+1
        return filename[index:]
    else:
        return ''

print(get_suffix('word.exe'))



#返回最大的两个数

def max2(x):
    m1, m2 = (x[0], x[1]) if x[0] > x[1] else (x[1], x[0])
    for index in range(2, len(x)):
        if x[index] > m1:
            m2 = m1
            m1 = x[index]
        elif x[index] > m2:
            m2 = x[index]
    return m1, m2

print(max2('1,4,2,7,3,0,4,8'))



#计算指定的年月日是这一年的第几天

def is_leap_year(year):
    return year % 4 == 0 and year % 100 == 0 or year % 400 == 0
def which_day(year, month, date):
    days_of_month = [
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
        [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ][is_leap_year(year)]
    total = 0
    for index in range(month - 1):   #下面累加不包括day_of_month[index]??
        total += days_of_month[index]
    return total + date

def main():
    print(which_day(2019,2,3))



#定义一个类描述数字时钟
from time import sleep

class Clock(object):
    def __init__(self, hour=0, min=0, sec=0):
        self._hour = hour
        self._min = min
        self._sec = sec

    def run(self):
        self._sec += 1
        if self._sec == 60:
            self._sec = 0
            self._min += 1
            if self._min == 60:
                self._min = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        return '%d:%d:%d' %(self._hour, self._min, self._sec)


def main():
    clock = Clock(23,59,57)
    while True:
        print(clock.show())
        sleep(1)
        clock.run()
"""

from math import sqrt

class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move_to(self, x1, y1):
        self.x1 = x1
        self.y1 = y1

    def move_by(self, dx, dy):
        self.dx = dx
        self.dy = dy

    def way(self):
        dx = self.x1 - self.x
        dy = self.y1 - self.y
        return sqrt(dx**2 + dy**2)

def main():
    p1 = Point(3, 5)
    p2 = Point()
    print(p1)
    print(p2)
    p2.move_by(-1, 2)
    print(p2)
    print(p1.way(p2))


if __name__ == '__main__':
    main()

