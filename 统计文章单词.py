file = open(r"C:\Users\Administrator\Desktop\Walden.txt","r")
lines = file.readlines()
# 把每行拆成单词
words = []
for line in lines:
    tmp_list = line.split(" ")
    for word in tmp_list:
        words.append(word.lower())
# 对words中出现一个元素出现个数
# 把统计结果保存到字典中，key是单词，value是单词出现的次数
words_count = {}
word_set = set(words)
for word in word_set:
    count_num = words.count(word)
    words_count[word] = count_num
# 对word_count字典排序，按照出现次数进行降序排序
sorted(words_count.items(),key=lambda item: item[1], reverse=True)