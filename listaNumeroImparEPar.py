# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 11:27:25 2022

@author: DISRCT
"""
numUsuario = 0

listaPar = []

listaImpar = []

for i in range(10):
    numUsuario = int(input("Digite 10 valores: "))
    if numUsuario % 2 == 0:
        listaPar.append(numUsuario)
    else:
        listaImpar.append(numUsuario)
        
print("Valores impares:", listaImpar)

print("\nValores pares:", listaPar)