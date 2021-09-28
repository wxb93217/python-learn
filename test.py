import msvcrt
height = float(input('输入身高（CM）：'))/100
weight = float(input('输入体重（KG）：'))
bmi = weight/height**2
if bmi<18.5:
    print('bmi=%.1f' % bmi,'过轻')
elif 25 > bmi >= 18.5:
    print('bmi=%.1f' % bmi,'正常')
elif 28 > bmi >= 25:
    print('bmi=%.1f' % bmi,'过重')
elif 28 > bmi >= 32:
    print('bmi=%.1f' % bmi,'肥胖')
else:
    print('bmi=%.1f' % bmi,'过胖')
print('感谢使用，任意键退出哦')
ord(msvcrt.getch())