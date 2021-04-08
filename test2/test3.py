# import sys
# for line in sys.stdin:
#     a = line.split()
#     print(int(a[0]) + int(a[1]))

count=0
while True:
    s=input().lower()
    l=input().lower()
    if len(s)>100:
        s=s[:101]
    if len(l)>500000:
        l=l[:500001]
    for i in s:
        for j in l:
            if i==j:
                count+=1
                break
    if count==len(s):
        print('s是l的有效字符串')
    else:
        print('s不是L的有效字符串')