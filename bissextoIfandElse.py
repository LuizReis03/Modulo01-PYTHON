# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 11:11:35 2022

@author: DISRCT
"""

ano = int(input("Digite o ano para verificar se é bissexto ou não: "))

if ano % 4 == 0:
    print("O ano é bissexto!")
elif ano % 100 != 0:
    print("O ano não e bissexto!")
elif ano % 400 != 0:
    print("O ano não e bissexto!")
    