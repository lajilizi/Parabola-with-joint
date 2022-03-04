# -*- coding: utf-8 -*-
"""
build 4/3/2022 15:46
@author: Li Zhengyi
"""

while 0<1:
    
    print("y=ax^2+bx+c,a≠0")
    a=int(input("a="))
    b=int(input("b="))
    c=int(input("c="))
    print("now type in the point")
    x1=int(input("x1="))
    x2=int(input("x2="))   #切线解析式y=(2a*x + b)*x - a*x^2 + c
    if a ==0:
        print("无效数据")
        continue
    if (x1 + b/(2*a))*(x2 - b/(2*a)) >= 0:
        print("无效数据")
        continue
    else:
        #解方程(2a*x1 + b)*x - a*x1^2=(2a*x2 + b)*x - a*x2^2
        h = abs(a*(x1^2 +x2^2 -2*x1*x2)/2)
        g = abs(x1 - x2)
        S1 = h*g/3
        print("S=",S1)