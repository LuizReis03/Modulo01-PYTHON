# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 11:14:58 2022

@author: DISRCT
"""

maior = []

menorDezoito = []

while True:
    nome = input("Digite um nome para o cadastro: ")
    if nome == "":
        break
    idade = int(input("Digite a idade: "))
    cpf = int(input("Digite o cpf: "))
    
    pessoa = {"nome": nome, "idade": idade, "cpf": cpf}
    maior.append(pessoa)
    
    
    if idade < 18:
        maior.remove(pessoa)
        menorDezoito.append(pessoa)
        
print("Maiores de 18:", maior)

print("Menores de 18:", menorDezoito)
        