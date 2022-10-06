# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 21:16:37 2022

@author: AngelTodorov
"""

print ("Въведи цената и дните до изтичане на винетка 1")

vignetteprice1 = float(input())
vignetteexpiration1 = int(input())

if vignetteprice1 > 50:
	print ("Взел сте си годишна винетка!")
else:
	 print ("Купи си годишна винетка!")
    
if vignetteexpiration1 < 10:
	 print ("Твоята винетка изтича, моля да я подновиш!")
else:
	 print ("Приятен път!")

print ("Въведи цената и дните до изтичане на винетка 2")
	 
vignetteprice2 = float(input())
vignetteexpiration2 = int(input())

if vignetteprice2 > 50:
	print ("Взел сте си годишна винетка!")
else:
	 print ("Купи си годишна винетка!")
    
if vignetteexpiration2 < 10:
	 print ("Твоята винетка изтича, моля да я подновиш!")
else:
	 print ("Приятен път!")