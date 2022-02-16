# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 10:28:52 2022

@author: disrct
"""

mr = 0

cr = 0

ar = 0

nulo = 0

branco = 0

print("------------ URNA ELETRÔNICA -------------")
opcao = int(input("Escolha uma opção: " + "\n1.Candidato Maria Santos" 
                  + "\n2.Candidato Carlos Silva" + "\n3.Candidato Ântonio Rocha" + 
                  "\n4.Nulo" + "\n5.Branco\n"))

while opcao != 7 and opcao != 0:
    if opcao == 1:
        mr =  mr + 1
        print("\nVocê votou em Maria Santos")
        
        opcao = int(input("Escolha uma opção: " + "\n1.Candidato Maria Santos" 
                  + "\n2.Candidato Carlos Silva" + "\n3.Candidato Ântonio Rocha" + 
                  "\n4.Nulo" + "\n5.Branco\n"))
        
    elif opcao == 2:
        cr =  cr + 1
        print("\nVocê votou em Carlos Silva")
        
        opcao = int(input("Escolha uma opção: " + "\n1.Candidato Maria Santos" 
                  + "\n2.Candidato Carlos Silva" + "\n3.Candidato Ântonio Rocha" + 
                  "\n4.Nulo" + "\n5.Branco\n"))
        
    elif opcao == 3:
        ar =  ar + 1
        print("\nVocê votou em Antônio Rocha")
        
        opcao = int(input("Escolha uma opção: " + "\n1.Candidato Maria Santos" 
                  + "\n2.Candidato Carlos Silva" + "\n3.Candidato Ântonio Rocha" + 
                  "\n4.Nulo" + "\n5.Branco\n"))
        
    elif opcao == 4:
        nulo =  nulo + 1
        print("\nVocê votou Nulo")
        
        opcao = int(input("Escolha uma opção: " + "\n1.Candidato Maria Santos" 
                  + "\n2.Candidato Carlos Silva" + "\n3.Candidato Ântonio Rocha" + 
                  "\n4.Nulo" + "\n5.Branco\n"))
        
    elif opcao == 5:
        branco =  branco + 1
        print("\nVocê votou Branco")
        
        opcao = int(input("Escolha uma opção: " + "\n1.Candidato Maria Santos" 
                  + "\n2.Candidato Carlos Silva" + "\n3.Candidato Ântonio Rocha" + 
                  "\n4.Nulo" + "\n5.Branco\n"))
        
    elif opcao == 6:
        print("Total de votos para Maria Santos:", mr)
        print("Total de votos para Carlos Silva:", cr)
        print("Total de votos para Antônio Rocha:", ar)
        print("Total de votos nulos:", nulo * 0.02 * 100, "%")
        print("Total de votos brancos:", branco * 0.02 * 100, "%")
        if mr > cr and mr > ar:
            print("\nMaria Santos é a vencedora!")
        elif cr > mr and cr > ar:
            print("\nCarlos Silva é o vencedor!")
        else:
            print("\nAntônio Rocha é o vencedor!")
        break
    
    
    
    
    
    
    
    
    