while True:
    soma = 0
    print('Digite um número, caso queira sair digite um número negativo!')
    numero = int(input('Digite o número que você deseja saber se é perfeito: \n'))
    if numero > 0:
        for divisor in range(1, numero):
            if numero % divisor == 0:
                soma += divisor

        if numero == soma:
            print(f'O número {numero} é perfeito! \n')
        else:
            print(f'O número {numero} não é perfeito! \n')
    else:
        break