# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 10:45:57 2022

@author: DISRCT
"""

numUsuario = 0

numImpar = 0

numPar = 0

while numUsuario < 1000:
    numUsuario = int(input("Digite números para somar: "))
    if numUsuario % 2 == 0:
        numPar = numImpar + numUsuario
    else:
        numImpar = numImpar + numUsuario
        

print("Soma de numeros impares:", numImpar)

print("Soma de numeros pares:", numPar)
