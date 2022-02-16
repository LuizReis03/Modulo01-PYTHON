# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 08:43:37 2022

@author: DISRCT
"""
print("Descubra quantos dias o mês possui\n")

numUsuario = int(input("Digite o numero do mês que deseja: "))

mes = ['Janeiro',
       'Fevereiro',
       'Março',
       'Abril',
       'Maio',
       'Junho',
       'Julho',
       'Agosto',
       'Setembro',
       'Outubro',
       'Novembro',
       'Dezembro']

if numUsuario > 12 or numUsuario < 0:
    print("Número inválido, tente novamente!!")
    
elif numUsuario == 2:
    print ("O mês de", mes[numUsuario - 1], "possui 28 dias.")
    
elif numUsuario % 2 != 0:
    print ("O mês de", mes[numUsuario - 1], "possui 31 dias.")
    
elif numUsuario > 7 and numUsuario % 2 == 0:
        print ("O mês de", mes[numUsuario - 1], "possui 31 dias.")
    
else:
    print ("O mês de", mes[numUsuario - 1], "possui 30 dias.")
     
    
