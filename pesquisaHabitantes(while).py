# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 10:59:33 2022

@author: disrct
"""

listaSexo = []

listaIdade = []

listaSalario = []

#SEXO
while True:
    #IDADE
    print("\nPara encerrar o sistema digite uma idade menor que 0")
    idade = int(input("\nDigite a idade: "))
    if idade > 0:
        listaIdade.append(idade)
    elif idade < 0:
        print("Sistema encerrado!")
        break
        
    #SEXO
    sexo = str(input("Digite o sexo: \nM-masculino \nF-feminino\n"))
    if sexo == 'm' or sexo == 'M':
        listaSexo.append(sexo)
    
    elif sexo == 'f' or sexo == 'F':
        listaSexo.append(sexo)
        qtdeMulher = listaSexo.count('F')

    
    salario = float(input("\nDigite o salário: "))
    
    listaSalario.append(salario)
    mediaSalario = sum(listaSalario) / len(listaSalario)
    
    menorSalario = min(listaSalario)
    iMenor = listaSalario.index(menorSalario)
    idadeMenor = listaIdade[iMenor]
    sexoMenor = listaSexo[iMenor]
    
        
    print("\n-------------------------")

        
    print("Media salário:", mediaSalario)
    
    print("A quantidade de mulheres é:", len(listaFem))
    
    print("A idade mínima é de:", listaIdade[iMenor], "e a idade máxima é de:", max(listaIdade))

    print("Menor salário igual a:", menorSalario)
    
    print("A idade da pessoa com menor salario:", idadeMenor)
    
    print("Sexo da pessoa com menor salário:", sexoMenor)
    
    print("-------------------------")
    
        
    