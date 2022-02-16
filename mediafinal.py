# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 11:02:38 2022

@author: DISRCT
"""

nomeAluno = input("Qual é seu nome?\n ")
nota1 = float(input("Qual o valor da sua primeira nota?\n "))
nota2 = float(input("Qual o valor da sua segunda nota?\n "))
nota3 = float(input("Qual o valor da sua terceira nota?\n "))
media = 0
calculoMedia = 0


calculoMedia = nota1 + nota2 + nota3 
media = calculoMedia / 3

print("Sua média final é de: ", media)

if (media >= 6.0):
    print("Voce está aprovado")
else:
    print("você está reprovado")
