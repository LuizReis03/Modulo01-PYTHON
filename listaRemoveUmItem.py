# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 11:18:16 2022

@author: DISRCT
"""

#PRIMEIRA LISTA
print("---------LISTA A---------")
valor1A = int(input("Digite o valor 1 da lista A: "))
valor2A = int(input("\nDigite o valor 2 da lista A: "))
valor3A = int(input("\nDigite o valor 3 da lista A: "))
valor4A = int(input("\nDigite o valor 4 da lista A: "))
valor5A = int(input("\nDigite o valor 5 da lista A: "))

listaA = []

listaA.insert(0, valor1A)
listaA.insert(1, valor2A)
listaA.insert(2, valor3A)
listaA.insert(3, valor4A)
listaA.insert(4, valor5A)

#SEGUNDA LISTA
print("\n\n---------LISTA B---------")
valor1B = int(input("Digite o valor 1 da lista B: "))
valor2B = int(input("\nDigite o valor 2 da lista B: "))
valor3B = int(input("\nDigite o valor 3 da lista B: "))
valor4B = int(input("\nDigite o valor 4 da lista B: "))
valor5B = int(input("\nDigite o valor 5 da lista B: "))

listaB = []

listaB.insert(0, valor1B)
listaB.insert(1, valor2B)
listaB.insert(2, valor3B)
listaB.insert(3, valor4B)
listaB.insert(4, valor5B)

listaC = listaA + listaB


print("item 1:", listaC[0], "\nitem 2:", listaC[1], "\nitem 3:", listaC[2],
      "\nitem 3:", listaC[2], "\nitem 4:", listaC[3], "\nitem 5:", listaC[4],
      "\nitem 6:", listaC[5], "\nitem 7:", listaC[6], "\nitem 8:", listaC[7],
      "\nitem 9:", listaC[8], "\nitem 10:", listaC[9])


removeLista = int(input("\nRemova um item da lista: "))

listaC.pop(removeLista - 1)
print(listaC, "\n")
