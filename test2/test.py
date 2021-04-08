# 输入n(数据的行数)
n=int(input())
count1=1
a=range(100)
# 初始化原始str
str='abcdfghijklmnopqrstuvwxyz'
# 确定n<=1000
while 1<=n<=1000:
    count2=0
    # 判定输入次数是否小于n
    while count1<=n:
        # 输入第count1次数据
        str1=input().lower()
        # 加密数据
        for s in str1:
            index1=str1.index(s)
            index2=str.index(s)
            a[0]=1
            a[1]=2
            a[2]=3
            # i<3时的加密方式
            if index1<3:
                s2=str[index2+a[index1]]
        #     i>3时的加密方式
            elif index1>=3:
                a[index1]=a[index1-1]+a[index1-2]+a[index1-3]
                s2=str[index2+a[index1]]
        #     打印加密过的数据
            print(s2)
        count1+=1