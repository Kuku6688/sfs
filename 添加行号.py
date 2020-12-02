file = open(r"C:\Users\Administrator\Desktop\stdent.csv","r")
lines = file.readlines()
# 给每行加行号
# 用#对齐
# 最长的行长度
max_len = 0
new_line
for line in lines
    if len(line)>max(line)
        max(line) = len(line)
print(max)
new_close
line_num = 1
for line in lines:
    line_num += 1
    tmp_line = line.rstrip() + "#" + str(line_num)
    print(tmp_line)