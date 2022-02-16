# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 10:49:21 2022

@author: DISRCT
"""
listaIdade = []

listaAltura = []

listaGeral = []

listaCalculo = []

i = 0

o = 0

for i in range(2):
    idade = int(input("Digite a idade: "))
    listaIdade.append(idade)

for c in range(2):
    altura = float(input("Digite a altura: "))
    listaAltura.append(altura)

mediaAltura = sum(listaAltura) / len(listaAltura)
for i in range(2):
    listaGeral.append(listaIdade[i])
    listaGeral.append(listaAltura[i])
    
    if listaIdade[i] > 13 and listaAltura[i] < mediaAltura:
        listaCalculo.append(listaIdade[i])
        listaCalculo.append(listaAltura[i])
        
print("\nTodos os alunos:", listaGeral)
print("Maiores de 13 anos abaixo da média:", len(listaCalculo) / 2, "aluno(s)")
print("Media das alturas:", mediaAltura)
