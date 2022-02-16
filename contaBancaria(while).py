# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 08:39:14 2022

@author: disrct
"""
saldo = 0

consultaSaldo = 0

saque = 0

deposito = 0

opcao = str(input("Escolha uma opção: \n(a)Consultar saldo \n(b)Saque \n(c)Depósito \n(d)Sair \n"))

while opcao != 'd':
    if opcao == 'a':
        print ("\nSaldo: R$", saldo)
        opcao = str(input("Escolha uma opção: \n(a)Consultar saldo \n(b)Saque \n(c)Depósito \n(d)Sair \n"))
        
    elif opcao == 'b':
        saque = int(input("\nQuanto deseja sacar? "))
        saldo = saldo - saque
        print("\nVocê sacou R$", saque)
        opcao = str(input("Escolha uma opção: \n(a)Consultar saldo \n(b)Saque \n(c)Depósito \n(d)Sair \n"))
        
    elif opcao == 'c':
        deposito = int(input("\nQuanto deseja depositar? "))
        saldo = saldo + deposito
        print("\nVocê depoistou R$", deposito)
        opcao = str(input("Escolha uma opção: \n(a)Consultar saldo \n(b)Saque \n(c)Depósito \n(d)Sair \n"))
    else:
        print("\nVocê saiu do programa")