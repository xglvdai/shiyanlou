# _*_ coding : UTF-8 _*_
#开发人员 ： 纠结中的忐忑
#开发时间 ： 2020/3/15  10:20
#文件名称 ： calculator.py.PY
#开发工具 ： PyCharm

import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Parameter Error')
        sys.exit()
    try:
        income = int(sys.argv[1])
    except ValueError:
        print('Parameter Error')
        sys.exit()
    value = income - 5000
    if value <= 0:
        result = 0
    elif value <= 3000:
        result = value * 0.03 - 0
    elif value <= 12000:
        result = value * 0.1 -210
    elif value <= 25000:
        result = value * 0.2 -1410
    elif value <= 35000:
        result = value * 0.25 -2660
    elif value <= 5500:
        result = value * 0.3 - 4410
    elif value <= 80000:
        result = value * 0.35 - 7160
    else:
        result = value * 0.45 -15160
    print(format(result,'.2f'))
