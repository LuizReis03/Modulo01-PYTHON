# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 10:39:25 2022

@author: DISRCT
"""

nota = float(input("Insira a nota: "))

if nota < 0.0:
    print("Verifique novamente o que foi digitado!")
    
elif nota > 10.0:
    print("Verifique novamente o que foi digitado!")
    
elif nota > 8.0 and nota <= 10.0:
    print("Parabéns, sua nota foi muito boa!")
    
elif nota >= 5.0 and nota <= 8.0:
    print("Nota azul!!")
    
elif nota < 5.0 and nota >= 0.0:
    print("Nota vermelha!!")
    
