# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 10:47:02 2022

@author: DISRCT
"""
peso1 = float(input("Digite o peso 1: "))
peso2 = float(input("\nDigite o peso 2: "))
peso3 = float(input("\nDigite o peso 3: "))
peso4 = float(input("\nDigite o peso 4: "))
peso5 = float(input("\nDigite o peso 5: "))

qtdePesos = []

qtdePesos.insert(0, peso1)
qtdePesos.insert(1, peso2)
qtdePesos.insert(2, peso3)
qtdePesos.insert(3, peso4)
qtdePesos.insert(4, peso5)

print("\nO maior peso inserido é", max(qtdePesos), "kg")

