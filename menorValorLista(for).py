# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 10:24:26 2022

@author: DISRCT
"""
resultado = 0

lista = []

for n in range(10):
    leNum = int(input("Digite 10 valores para achar o menor e maior: "))
    lista.append(leNum)
    
print("\nMenor valor da lista:", min(lista))

print("\nMaior valor da lista:", max(lista))