# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 09:39:56 2022

@author: disrct
"""

opcao = str(input("Escolha uma operação: \n(+)Soma \n(-)Subtração \n(*)Multiplicação \n(/)Divisão \n"))

while opcao == '+' or opcao == '-' or opcao == '*' or opcao == '/':
    if opcao == '+':
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("\nDigite o segundo número: "))
        result = num1 + num2
        print("\nO resultado é:", result)
        break
    
    elif opcao == '-':
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("\nDigite o segundo número: "))
        result = num1 - num2
        print("\nO resultado é:", result)
        break
        
    elif opcao == '*':
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("\nDigite o segundo número: "))
        result = num1 * num2
        print("\nO resultado é:", result)
        break
        
    elif opcao == '/':
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("\nDigite o segundo número: "))
        result = num1 / num2
        print("\nO resultado é:", result)
        break