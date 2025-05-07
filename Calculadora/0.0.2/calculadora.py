import os
from time import sleep

def soma(a,b):
    return a+b

def divisao(a,b):
    return a/b

def multiplicacao(a,b):
    return a*b

def subtracao(a,b):
    return a-b

def potenciacao(a,b):
    return a**b

def raiz_quadrada(a):
    return a**(1/2)

def float_to_int(resultado):
    if type(resultado) == float:
        return int(resultado)
    else:
        return resultado
def limpar_terminal():
    os.system('cls')
def wait(a):
    for x in range(a):
        print('.', flush=True)
        sleep(0.5)

print('Olá, seja bem-vindo(a) à minha calculadora!\nv0.0.2\n')
sleep(0.5)
listaoperacoes = ['soma','subtracao','multiplicacao','divisao']
listaoperacoesformatada = ['Soma','Subtração','Multiplicação','Divisão']
menu = True
operacao = 0
while menu == True: #Loop para realizar as operações básicas
    sleep(0.5)

    #Coletando a operação que será feita
    while operacao not in range(1,5):
            try:
                print('Qual operação gostaria de realizar?\n')
                sleep(0.5)
                print(f'[1]:{listaoperacoesformatada[0]}', end =' ')
                print(f'[2]:{listaoperacoesformatada[1]}', end =' ')
                print(f'[3]:{listaoperacoesformatada[2]}', end =' ')
                print(f'[4]:{listaoperacoesformatada[3]}')
                operacao = int(input('Sua resposta: '))
                if operacao not in range(1,5):
                    print('\nDigite um valor válido!\n')
                print()
            except ValueError:
                sleep(0.5)
                print('\nErro: Você não digitou um número válido.\n')

    #Coletando os números que serão calculados
    while True:  #Loop do primeiro número
        try:   
            a = float(input('Primeiro valor: '))
            if type(a) == float:
                break
        except ValueError:
            sleep(0.5)
            print('\nErro: Você não digitou um número válido.\n')

    while True:  #Loop do segundo número
        try:   
            b = float(input('Segundo valor: '))
            if operacao == 4 and b == 0:
                print('Não podes dividir por 0!')
                continue
            break
        except ValueError:
            sleep(0.5)
            print('\nErro: Você não digitou um número válido.\n')
    
    #Realizar a operação
    for i in listaoperacoes:
        if i == listaoperacoes[operacao-1]:
            resultado = globals()[i](a,b)
    #Print resultado
    wait(3)
    if resultado % 1 == 0: 
        print(float_to_int(resultado))
    else:
        print(resultado)
    #Perguntar se quer fazer outra operação
    sleep(0.5)
    while True:
        print('\nGostaria de realizar outra operação?\n')
        print('[1]: Sim [2]: Não')
        try:
            operacao = int(input('Sua resposta: '))
            if operacao == 1:
                print('Reiniciando o sistema...')
                wait(3)
            else:
                print('Encerrando o sistema...')
                wait(2)
                menu = False
            break
        except ValueError:
            print('Digite um valor válido!')
    operacao = 0
    limpar_terminal()
            