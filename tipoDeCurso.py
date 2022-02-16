# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 08:29:42 2022

@author: DISRCT
"""

nomeAluno = input("Qual é seu nome?")

diasSemana = int(input("\nQuantos dias na semana pretende fazer?"))

valorTot = 0

tipoCurso = int(input("Digite 1 para curso básico" + "\nDigite 2 para intermediario" + "\nDigite 3 para avançado\n"))

if tipoCurso == 1:
    valorTot = (diasSemana * 7) * 15
    print("Olá", nomeAluno, ", o valor a ser pago é de: R$", valorTot)
    
elif tipoCurso == 2:
    valorTot = (diasSemana * 8.5) * 20
    print("Olá", nomeAluno, ", o valor a ser pago é de: R$", valorTot)
    
elif tipoCurso == 3:
    valorTot = (diasSemana * 10) * 25
    print("Olá", nomeAluno, ", o valor a ser pago é de: R$", valorTot)