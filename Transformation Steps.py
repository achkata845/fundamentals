# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 22:06:22 2022

@author: AngelTodorov
"""

print ("Направи ли стъпка 1? (експорт на файловете)")

step1 = str(input())

if step1 == "да":
	print ("Премини към стъпка 2")
elif step1 == "не":
	print ("Направи стъпка 1")
else:
	print ("Отговори или с да или с не")


print ("Направи ли стъпка 2? (промени по файловете)")

step2 = str(input())

if step2 == "да":
	print ("Премини към стъпка 3")
elif step2 == "не":
	print ("Направи стъпка 2")
else:
	print ("Отговори или с да или с не")


print ("Направи ли стъпка 3? (обновяване Power BI)")

step3 = str(input())

if step3 == "да":
	print ("Power BI е обновен")
elif step3 == "не":
	print ("Направи стъпка 3")
else:
	print ("Отговори или с да или с не")