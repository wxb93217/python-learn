#解一元二次方程-打包
import msvcrt
import math
print('计算一元二次方程:\nax^2+bx+c=0')
a=float(input('输入a='))
b=float(input('输入b='))
c=float(input('输入c='))
def quadratic(a,b,c):
    try:
        n = (-b+math.sqrt(b**2-4*a*c))/(2*a)
        n2 = (-b-math.sqrt(b**2-4*a*c))/(2*a)
        return n , n2
    except ValueError:
        err='没有答案，负数平方根是开不出来哒T T'
        return err
print('答案x=',quadratic(a,b,c))

print('感谢使用，任意键退出哦')
ord(msvcrt.getch())