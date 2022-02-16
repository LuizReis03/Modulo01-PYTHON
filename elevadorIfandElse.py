# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 11:00:43 2022

@author: DISRCT
"""

capacidadePeso = float(input("Qual a capacidade máxima que o elevador aguenta?\n"))

pessoa1 = float(input("Digite o peso da primeira pessoa: "))
pessoa2 = float(input("Digite o peso da segunda pessoa: "))
pessoa3 = float(input("Digite o peso da terceira pessoa: "))
pessoa4 = float(input("Digite o peso da quarta pessoa: "))
pessoa5 = float(input("Digite o peso da quinta pessoa: "))

guardaPesoPessoa = pessoa1 + pessoa2 + pessoa3 + pessoa4 + pessoa5

if guardaPesoPessoa > capacidadePeso:
    print("A carga suportada pelo elevador foi excedida! Necessário que desça alguém!")
    
else:
    print("\nO peso total é de: ", guardaPesoPessoa)
    print("\nLiberado para subir!")