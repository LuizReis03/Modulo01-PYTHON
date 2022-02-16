# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 09:47:29 2022

@author: DISRCT
"""
import math

def operacoes(numUsuario):
     raiz = math.sqrt(numUsuario)
     print("\nA raiz quadrada de", numUsuario, "é: {:.2f}".format(raiz))
     
     quadrado = numUsuario * numUsuario
     print("\nO quadrado do numero", numUsuario, "é: {:.2f}".format(quadrado))
     
     inverso = numUsuario **-1
     print("\nO inverso do numero", numUsuario, "é: {:.2f}".format(inverso))
     
     fatorial = math.factorial(numUsuario)
     print("\nO fatorial do numero", numUsuario, "é: {:.2f}".format(fatorial))
        
print(operacoes(int(input("Digite um número: "))))

        