# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 09:03:38 2022

@author: DISRCT
"""


num1, num2, num3, num4, num5 = map(int, input("Digite 5 valores númericos: ").split())

pala1, pala2, pala3, pala4, pala5 = map(str, input("\nDigite 5 palavras: ").split())

lista_numero = []
lista_numero.insert(0, num1)
lista_numero.insert(1, num2)
lista_numero.insert(2, num3)
lista_numero.insert(3, num4)
lista_numero.insert(4, num5)


lista_string = []
lista_string.insert(0, pala1)
lista_string.insert(1, pala2)
lista_string.insert(2, pala3)
lista_string.insert(3, pala4)
lista_string.insert(4, pala5)


lista_geral = lista_numero + lista_string

lista_geral = sorted(lista_numero)

print("\n"+ "\n", lista_geral)

lista_geral = sorted(lista_string)

print("\n"+ "\n", lista_geral)
