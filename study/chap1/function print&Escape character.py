# 创建人：gw
# 开发时间：2022/6/24 11:39


#print函数
print(520) #print可以输出数字，不用加引号
print('helloworld')
print('3+1') #print可以输出字符串，需要加引号
print(3+1) #print可以输出含有运算符的表达式，不需要加引号

#将数据输出到文件中 注意点：1.所指定的盘符存在 2.使用file=
fp=open('D:/text.txt','a+') #a+的含义：如果没有text.txt文件，则创建一个，有则在原有内容上追加
print('helloworld',file=fp)
fp.close()
#不进行换行输出，即输出内容在一行之中
print('hello','world','Python')


#转义字符
print('hello\nworld') #\n代表换行，newline的首字母
print('hello\tworld') #\t代表跳到下一个制表位，每个制表位代表4个字符的位置
print('hello\rworld') #\r代表回车，将hello进行覆盖
print('hello\bworld') #\b代表退一个格

print('http:\\\\www.baidu.com') #在反斜杠前面加反斜杠，代表一个反斜杠是要输出的内容
print('她说：\'她静悄悄地来过\'') #在引号前面加反斜杠，代表这个引号是要输出的内容

#原字符：不希望字符串中的转义字符起作用，就使用原字符，在字符串之前加r或R
print(r'hello\nworld')
#注意事项：最后一个字符不能是反斜杠，但可以是两个反斜杠，这样代表将反斜杠作为字符输出
#如print(r'hello\nworld\')
print(r'hello\nworld\\')
