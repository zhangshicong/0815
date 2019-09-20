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


"""





