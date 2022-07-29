# 创建人：gw
# 开发时间：2022/7/5 14:16

"""
continue语句：用于结束当前循环，进入下一次循环，通常与if一起使用
"""
#输出1到50之间所有5的倍数
for item in range(1,51):
    if item % 5 != 0:
        continue
    else:
        print(item)

