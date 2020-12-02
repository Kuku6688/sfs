# 创建字典student，keyx学好
file = open(r'C:\\Users\\Administrator\\Desktop\\stdent.csv','r')
# 读取文件
lines = file.readlines()
student = {}
for line in lines:
    tmp_list = line.split(',')
    xuehao = tmp_list[0]
    xingming = tmp_list[1]
    student[xuehao]=xingming
# 抽取学号
import random
num = int(input("输入人数:"))
xuehao_list = random.sample(student.keys(),num)
# 如何把字典转唤成列表
xuehao_list  
# 根据随机抽取的学号，输出
for xuehao in xuehao_list:
    print(student[xuehao])