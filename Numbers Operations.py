# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 21:29:13 2022

@author: AngelTodorov
"""

print ("Въведи число а")

a = int(input())

print ("Въведи число b")

b = int(input())

print ("Въведи операция")

operation = str(input())

if operation == "събиране":
    print (a + b)

elif operation == "изваждане":
    print (a - b)

elif operation == "умножение":
    print (a * b)

elif operation == "деление":
    print (a / b)

elif operation == "степенуване":
    print (a ** b)

elif operation == "коренуване":
    print ("Импортнете math")

elif operation == "логаритмуване":
    print ("Импортнете math")

else:
    print ("Операцията не съществува")