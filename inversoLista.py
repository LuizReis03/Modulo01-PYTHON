# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 11:36:47 2022

@author: DISRCT
"""
numUsuario = 0

lista = []

for i in range(8):
    numUsuario = int(input("Digite 8 numeros: "))
    lista.append(numUsuario)
    
lista.reverse()
print(lista)