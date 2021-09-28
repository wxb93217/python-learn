#循环去除首尾空格
def trim(s):
    i=0
    l=len(s)
    while i<l:
        if s[:1]==' ':
            s=s[1:]
        elif s[-1:]==' ':
            s=s[:-1]
        else:
            break
        i=i+1
    return s

# 测试:
if trim('hello  ') != 'hello':
    print('测试失败1!')
elif trim('  hello') != 'hello':
    print('测试失败2!')
elif trim('  hello  ') != 'hello':
    print('测试失败3!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败4!')
elif trim('') != '':
    print('测试失败5!')
elif trim('    ') != '':
    print('测试失败6!')
else:
    print('测试成功!')