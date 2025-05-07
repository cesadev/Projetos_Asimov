from random import randint
voce = 0
computador = 0

dicio = {
    0: 'Pedra',
    1: 'Papel',
    2: 'Tesoura'
         }

def inicio():
    print("==================================================")
    print("Bem-vindo(a) ao jogo de Pedra, Papel ou Tesoura.")
    print("==================================================")
    print()
    print('PLACAR:')
    print(f'Você: {voce}')
    print(f'Computador: {computador}')
    print()
    return

def bot_choice():
    bot = randint(0, 2)
    return bot

def user_choice():
    print('Escolha o seu lance:')
    print('0 - Pedra | 1 - Papel | 2 - Tesoura')
    resposta = int(input('Sua resposta: '))
    return resposta

while True:
    inicio()
    bot = bot_choice()
    resposta = user_choice()

    print(f'Sua escolha = {dicio.get(resposta)}, Escolha do Bot = {dicio.get(bot)}')
    if resposta == bot + 1 or resposta == bot - 2:
        voce += 1
        print('Você Venceu!')
    elif bot == resposta + 1 or bot == resposta - 2:
        computador += 1
        print('O Computador Venceu!')
    elif bot == resposta:
        print('Empate!')
    
    print('Deseja continuar jogando? 1 - SIM | 2 - NÃO')
    continuar = int(input('Sua resposta: '))
    
    if continuar == 2:
        print('Encerrando!')
        break
    elif continuar == 1:
        print('Reiniciando!')