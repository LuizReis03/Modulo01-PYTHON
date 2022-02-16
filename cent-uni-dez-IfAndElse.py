# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 11:29:31 2022

@author: DISRCT
"""

num = int(input("Digite um número menor que 1000: "))

uni = num % 10

dez = num % 100 - uni

cent = num % 1000 - dez - uni

if num > 1000:
    print("Você digitou um numero maior que 1000, por favor digite outro")

print("Unidade:", uni)
print("Dezena:", dez//10)
print("Centena:", cent//100)


