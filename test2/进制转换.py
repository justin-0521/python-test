# a=int(input(),base=16)
# print(a)
#
while True:
    #     输入字符串
    str1 = input()
    #     如果字符串长度大于8，输出前八个字符

    while len(str1) > 8:
        print(str1[:8])
        str1 = str1[8:]
    #         如果字符串长度小于从左至右用0补齐
    else:
        print(str1.ljust(8, '0'))
