# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 09:20:38 2022

@author: DISRCT
"""
import random

numAleatorio = random.randint(1, 3)

pedra = 0

papel = 0

tesoura = 0

vitorias = 0

score = 0


while True:
    escolha = str(input("Você deseja ser pedra, papel ou tesoura? "))
    #verifica entrada (par ou impar)
    if escolha != 'pedra' and escolha != 'papel' and escolha != 'tesoura':
        print("\nVerifique o que foi digitado...")
        continue
    
    numJogador = int(input("Digite um número: "))
    print("A máquina jogou:", numAleatorio)
    
    compara = numJogador + numAleatorio
    
    if escolha == 'par' and compara % 2 == 0:
        vitorias += 1
        score += 3
        print("Jogador ganhou!")
        continue
    elif escolha == 'impar' and compara % 2 != 0:
        vitorias += 1
        score += 3
        print("Jogador ganhou!")
        continue
    
    elif escolha == 'par' and compara % 2 != 0:
        print("VOCÊ PERDEU!")
        continuaJogando = str(input("\nDeseja continuar? (s/n) "))
    elif escolha == 'impar' and compara % 2 == 0:
        print("VOCÊ PERDEU!")
        continuaJogando = str(input("\nDeseja continuar? (s/n) "))
        
    if continuaJogando != 's' and continuaJogando != 'n':
        print("\nVerifique o que foi digitado...")
    elif continuaJogando == 's':
        continue
    elif continuaJogando == 'n':
        break


print("\nNÚEMERO DE VITÓRIAS:", vitorias)
print("SCORE:", score)
    