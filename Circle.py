# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 16:49:54 2022

@author: AngelTodorov
"""

print("Enter circle's radius: ")
r = float(input())

p = float(3.14)
rsq = r**2

s = p*rsq
p = 2*p*r

expression1= "Circle's face is "
expression2 = "Circle's perimeter is "

print(expression1 + str(s))
print(expression2 + str(p))