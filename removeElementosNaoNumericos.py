# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 08:20:12 2022

@author: DISRCT
"""
nome1 = input("Digite o primero nome: ")
tel1 = int(input("\nDigite o primeiro numero de telefone: "))
idade1 = int(input("\nDigite a primeira idade: "))

nome2 = input("Digite o segundo nome: ")
tel2 = int(input("\nDigite o segundo numero de telefone: "))
idade2 = int(input("\nDigite a segunda idade: "))

lista = []

lista.insert(0, nome1)
lista.insert(1, tel1)
lista.insert(2, idade1)

lista.insert(3, nome2)
lista.insert(4, tel2)
lista.insert(5, idade2)

if nome1.isdigit() == False:
    lista.remove(nome1)
    
if nome2.isdigit() == False:
    lista.remove(nome2)

print("\n", lista)