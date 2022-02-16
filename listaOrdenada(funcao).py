# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 08:16:26 2022

@author: DISRCT
"""
import random
lista = []
listaOrd = []

def numALeatorio(num1, num2):
    aleatorio = random.randint(num1, num2)
    return aleatorio

limiteInferior = int(input("Digite o limite inferior: "))
limiteSuperior = int(input("Digite o limite superior: "))
tamLista = int(input("Digite o tamanho da lista: "))

for i in range(tamLista):
    controla = numALeatorio(limiteInferior, limiteSuperior)
    lista.append(controla)
    
print("\nLista:", lista)

for i in range(tamLista):
    listaOrd.append(min(lista))
    lista.remove(min(lista))

print("\nLista ordenada:", listaOrd)