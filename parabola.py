# -*- coding: utf-8 -*-
"""
build 6/3/2022 12:31
@author: Li Zhengyi
"""

while 0<1:
    
    print("y=ax^2+bx+c,a≠0")
    a=float(input("a="))
    print("now type in the joint")
    x1=float(input("x1="))
    x2=float(input("x2="))   #切线解析式y=(2a*x + b)*x - a*x^2 + c
    if a ==0:
        print("无效数据")
        continue
    
    else:
        #解方程(2a*x1 + b)*x - a*x1^2=(2a*x2 + b)*x - a*x2^2
        h = abs(a*(x1*x1 +x2*x2 -2*x1*x2)/2)
        g = abs(x1 - x2)
        S1 = h*g/3
        print("S=",round(S1,3))