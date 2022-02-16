# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 08:13:14 2022

@author: disrct
"""

num_igual = False

lista = []

while num_igual == False:
    n = int(input("Insira um valor: "))
    for i in lista:
        if n == i:
            num_igual = True
            break
    lista.append(n)
        
print("\nA soma dos valores digitados:", sum(lista))