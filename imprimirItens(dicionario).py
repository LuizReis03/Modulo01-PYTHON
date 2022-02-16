# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 11:36:57 2022

@author: DISRCT
"""
i = 1

dicionario = {}

while True:
    nome = input("Digite um nome para o cadastro: ")
    if nome == "":
        break
    idade = int(input("Digite a idade: "))
    cpf = int(input("Digite o CPF: "))

    pessoa = {"nome": nome, "idade": idade, "cpf": cpf}
    
    contador = "Pessoa " + str(i)
    i = i + 1
    dicionario [contador] = pessoa
    
type(dicionario)
dict()
print(dicionario)