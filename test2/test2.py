n=float(input('请输入一个正浮点数'))
if (n-int(n))*10>=5:
    print(f'该浮点数的近似值是{int(n)+1}')
else:
    print(f'该浮点数的近似值是{int(n )}')