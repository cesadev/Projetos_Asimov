#Jogo da Velha
from random import randint
import os
def escolher_dificuldade():
    while True:
        try:
            print('Escolha a dificuldade: ')
            print('[1] Fácil, [2] Média, [3] Difícil')
            escolha_dificuldade = int(input('Sua escolha: '))
            if escolha_dificuldade in [1,2,3]:
                return escolha_dificuldade
                break
            else:
                print('Digite um valor válido!')
        except ValueError:
            print('Digite um valor válido!')
def escolher_quem_comeca():
    while True:
        try:
            print('Quem começa?')
            print('[1] Você, [2] Computador')
            escolha_iniciador = int(input('Sua escolha: '))
            if escolha_iniciador in [1,2]:            
                return escolha_iniciador
            else:
                print('Digite um valor válido')
        except ValueError:
            print('Digite um valor válido!')

def quemcomeca(jogador):
    if jogador == 1:
        ordem = {
            '1': jogada_player,
            '2': jogada_bot,
            '3': True
        }
        print('O Jogador começará!')
    else:
        ordem = {
            '1': jogada_bot,
            '2': jogada_player,
            '3': False
        }
        print('O Bot começará!')
    return ordem

def tabuleiro(lista):
    os.system('cls')
    for i in range(1, 10):
        if i in [3,6,9]:
            print(lista[str(i)])
        else:
            print(lista[str(i)], end = '  ')

def jogada_bot(lista):
    while True:
        escolhabot = randint(1, 9)
        print(f'escolha do bot = {escolhabot}')
        if lista[str(escolhabot)] in ['x','o']:
            print('Valor inválido! Já escolhido antes!')
            tabuleiro(lista)
        else:
            break
    print(f'bot escolheu: {escolhabot}')
    return escolhabot

def jogada_player(lista):
    while True:
        try:
            while True:
                escolhaplayer = int(input('Sua escolha: '))
                print(f'escolha do player = {escolhaplayer}')
                if lista[str(escolhaplayer)] in ['x','o']:
                    print('Valor inválido! Já escolhido antes!')
                    tabuleiro(lista)
                else:
                    break
            return escolhaplayer
        except ValueError:
            print('Digite um valor Válido!')

def transformarlista(ordem, escolha, lista):
    if ordem == 1:
        lista[str(escolha)] = 'x'
    elif ordem == 2:
        lista[str(escolha)] = 'o'

def checar_vitoria(lista):
    vitoria = False
    for i in range(1,7+1,3):
        listateste = []
        listateste2 = []
        for x in range(3):
            listateste.append(x+i)
            listateste2 = [lista[str(listateste[0])],lista[str(listateste[1])], lista[str(listateste[2])]]
            if listateste2[0] == listateste2[1] == listateste2[2]:
                if listateste2[0] == 'x':
                    vencedor = 1
                elif listateste2[0] == 'o':
                    vencedor = 2
                print('Vitoria horizontal!')
                vitoria = True

    for i in range(1,4):
        listateste = []
        for x in range(0,7,3):
            listateste.append(x+i)
            listateste2 = [lista[str(listateste[0])],lista[str(listateste[1])], lista[str(listateste[2])]]
            if listateste2[0] == listateste2[1] == listateste2[2]:
                if listateste2[0] == 'x':
                    vencedor = 1
                elif listateste2[0] == 'o':
                    vencedor = 2
                print('Vitória vertical')
                vitoria = True

    if lista[str(1)] == lista[str(5)] == lista[str(9)] or lista[str(3)] == lista[str(5)] == lista[str(7)]:
        print('Vitoria diagonal')
        vitoria = True
    if vitoria:
        if jogador == vencedor:
            print('Jogador Venceu!')
        else:
            print('Bot Venceu!') 
    return vitoria

lista = {
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9
    } 
jogador = escolher_quem_comeca()
ordem = quemcomeca(jogador)
tabuleiro(lista) # mostra tabuleiro
vitoria = False
while not vitoria:
    for x in range(1,7):
        for i in range(1,3):
            escolha = ordem[str(i)](lista)
            transformarlista(i,escolha,lista)
            tabuleiro(lista)
            vitoria = checar_vitoria(lista)
            if vitoria:
                print('Fim de Jogo, porra')
                break
        if vitoria:
            break
    break
    
