# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 10:52:18 2022

@author: disrct
"""
numUsuario = int(input("Digite um número: "))
anterior = 0
proximo = 0

while proximo < numUsuario:
  print(proximo)
  proximo = proximo + anterior
  anterior = proximo - anterior
  if(proximo == 0):
       proximo = proximo + 1