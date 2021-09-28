#解一元二次方程
import math
def quadratic(a,b,c):
    n = (-b+math.sqrt(b**2-4*a*c))/(2*a)
    n2 = (-b-math.sqrt(b**2-4*a*c))/(2*a)
    return n , n2
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')