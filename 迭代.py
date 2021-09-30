# -*- coding: utf-8 -*-
from collections.abc import Iterable

def findMinAndMax(L):
    MIN=0
    MAX=0
    if isinstance(L, Iterable) and L:
        for i, value in enumerate(L):
            if i==0:
                MIN=value
                MAX=value
            elif value>=MAX:
                MAX=value
            elif value<=MIN:
                MIN=value
            else:
                pass
        L=(MIN, MAX)
    else:
        L=(None, None)
    print(L)
    return L
# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败1!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败2!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败3!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败4!')
else:
    print('测试成功!')