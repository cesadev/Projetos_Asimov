"""
Operações:
1: soma
2: subtração
3: multiplicação
4: divisão
5: potenciação
"""
import time
operacao = 0
continuarop = 0
operacoes = ['soma','subtração','multiplicação','divisão','potenciação']

while operacao == 0: #Se não tiver operação, iniciar o programa.
    print('Escolha a operação:\n[1]: Soma\n[2]: Subtração\n[3]: Multiplicação\n[4]: Divisão\n[5]: Potenciação\n')
    operacao = int(input('Sua opção: '))
    
    try:
        operacao = int(input("Sua opção: "))
        if operacao in range(1, 6):  # Checando se está entre 1 e 5
            print(f"Você escolheu a operação {operacao}.")
        else:
            print("Escolha um número entre 1 e 5!")
            operacao = 0
    except ValueError:
        print("Erro: você deve digitar um número válido!")
        operacao = 0

    if operacao not in [1,2,3,4,5]: #Checando se escolheu operação válida.
        print('Escolha um valor válido!')
        time.sleep(1)
        operacao = 0
    
    while operacao != 0:
        time.sleep(0.5)
        print(f'\nDeseja mesmo realizar uma operação de {operacoes[operacao - 1]}?\n')
        print('[1]: Sim\n[2]: Não')
        time.sleep(0.5)
        continuarop = int(input('\nSua opção: '))
        if continuarop == 2:
            break
        time.sleep(0.5)
        num1 = float(input('\nPrimeiro número: '))
        num2 = float(input('Segundo número: '))
        time.sleep(0.5)

        if operacao == 1: #Realizando a operação baseada na escolha do usuário:
            print(f'\n\n{num1} + {num2} = {num1+num2}')
        elif operacao == 2:
            print(f'\n\n{num1} - {num2} = {num1-num2}')
        elif operacao == 3:
            print(f'\n\n{num1} x {num2} = {num1*num2}')
        elif operacao == 4:
            print(f'\n\n{num1} / {num2} = {num1/num2}')
        else:
            print(f'\n\n{num1} ** {num2} = {num1**num2}')
        break #Encerra o loop while de operação

    operacao = int(input('\nDeseja realizar outra operação?\n[1]: Sim\n[2]: Não\nSua resposta: '))
    time.sleep(0.5)
    if operacao == 1:
        operacao = 0
        print('Reiniciando...')
    else:
        print('Encerrando...')