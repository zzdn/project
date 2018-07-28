#encoding=UTF-8
import random
KING  = ['大王','小王']
#生成牌数2到10
heitao = hongtao = meihua = fangkuai = range(2,11)
#生成牌数JQKA
heitao2 = hongtao2 = meihua2 = fangkuai2 = ['A','J','Q','K']
nums =[]
for x in heitao:
    x = str(x)
    nums.append(x)
HEITAO = nums + heitao2
HeT =[]
for x in HEITAO:
     re = '黑桃'+x
     HeT.append(re)

nums =[]
for x in hongtao:
    x = str(x)
    nums.append(x)
HONGTAO = nums + hongtao2
HoT =[]
for x in HONGTAO:
     re = '红桃'+x
     HoT.append(re)

nums =[]
for x in meihua:
    x = str(x)
    nums.append(x)
MEIHUA = nums + meihua2
MH =[]
for x in HEITAO:
     re = '梅花'+x
     MH.append(re)

nums =[]
for x in fangkuai:
    x = str(x)
    nums.append(x)
FANGKUAI = nums + fangkuai2
FK =[]
for x in FANGKUAI:
     re = '方块'+x
     FK.append(re)

paishu = (HeT+HoT+MH+FK+KING)
random.shuffle(paishu)
num1 = []
num2 = []
num3 = []
n = 1
while n <=17:
    result = paishu.pop()
    num1.append(result)
    n +=1

m = 1
while m <=17:
    result2 = paishu.pop()
    num2.append(result2)
    m +=1

h = 1
while h <=17:
    result3 = paishu.pop()
    num3.append(result3)
    h +=1

print('玩家一的牌是：{0}\n\t 张数是: {1}张'.format(num1,len(num1)))
print('玩家二的牌是：{0}\n\t 张数是: {1}张'.format(num2,len(num2)))
print('玩家三的牌是：{0}\n\t 张数是: {1}张'.format(num3,len(num3)))
print('底牌是：{0}\n\t 张数是: {1}张'.format(paishu,len(paishu)))

