import random
list1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
a=int(input("输入一个数："))
ln = len(list1)
a = random.sample(list1,a)
print(a)