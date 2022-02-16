# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 10:48:27 2022

@author: DISRCT
"""

consumoMedio = 0
disTotal = int(input("Qual foi a ditância total percorrida? (Em km)\n " ))
totCombustivel = int(input("Qual foi o total de combustível gasto? (Em litros)\n " ))

consumoMedio = disTotal / totCombustivel

print ("O consumo médio feito pelo veículo foi de:\n", consumoMedio, "Km/l")

