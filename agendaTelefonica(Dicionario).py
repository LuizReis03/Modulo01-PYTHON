# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 10:34:03 2022

@author: DISRCT
"""


agenda = []


while True:
    nome = input("Digite um nome: ")
    if nome == "":
        break
    tel = int(input("Digite um numero de telefone: "))
    pessoa = {"Nome": nome, "Telefone": tel}
    agenda.append(pessoa)
    
print(agenda, "\n")
    