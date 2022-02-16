# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 11:21:09 2022

@author: DISRCT
"""
listaMes = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto',
            'Setembro', 'Outubro', 'Novembro', 'Dezembro']

listaTemp = []

for i in listaMes:
    print("\n", i)
    temperatura = float(input("Digite a temperatura do mês: "))
    listaTemp.append(temperatura)
    
for temp in listaTemp:
    mediaTemp = sum(listaTemp) / len(listaTemp)

print("\nMédia anual de temperatura:", mediaTemp)
