# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 09:11:16 2022

@author: DISRCT
"""

while True:
    numUsuario = int(input("Digite um valor: "))
    if numUsuario % 10 == 0:
        print("Esse número é multiplo de 10")
    if numUsuario < 0:
        print("Programa encerrado!")
        break
    