# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 11:40:20 2022

@author: DISRCT
"""
numUsuario = 0

for i in range(10):
    numUsuario = int(input("Digite 10 numeros: "))
    if numUsuario < 0:
        numUsuario = numUsuario * 0
        print(numUsuario)