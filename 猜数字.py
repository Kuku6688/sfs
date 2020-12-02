import random
n=random.randint(1, 100)
i=1
while i<=5:
    a =  int(input('输入一个大于0小于100的数:'))
    if(a>n) :
        print('你输入的数太大了')
        i=i+1
    elif(a<n):
        print('你输入的数太小了')
        i=i+1
    elif(a==n):
        print("猜对啦")
        break
    elif(i==5):
        print("猜了5次了")
        break