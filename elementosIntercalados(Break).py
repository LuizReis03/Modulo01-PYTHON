# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 10:39:59 2022

@author: DISRCT
"""
lista1 = []

lista2 = []

i = 0

o = 0

while True:
    if i < 10:
        elemento_lista1 = str(input("Digite 10 elementos para lista 1: "))
        lista1.append(elemento_lista1)
        i += 1
        continue
        print("\n")
    elif o < 10:
        elemento_lista2 = str(input("Digite 10 elementos para lista 2: "))
        lista2.append(elemento_lista2)
        o += 1
        continue
    else:
        listaGeral = [*sum(zip(lista1, lista2), ())]
        print("\nLista misturada:", listaGeral)
        break