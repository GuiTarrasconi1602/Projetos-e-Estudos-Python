
while True:
    crescente = True
    numeros = []
    ultimomes = 0

    meses = int(input('Digite a quantidade de índices de audiência serão digitados: '))
    for n in range(0, meses):
        audiencia = float(input(f'Digite a {n + 1}° audiência: '))
        if audiencia >= ultimomes:
            ultimomes = audiencia
            numeros.append(audiencia)
        else:
            crescente = False
            ultimomes = audiencia
            numeros.append(audiencia)

    if crescente:
        print('AUDIÊNCIA SEMPRE CRESCENTE.')
    else:
        print('AUDIÊNCIA NEM SEMPRE CRESCENTE.')

    media = sum(numeros)/len(numeros)
    print(f'Média de audiência: {round(media, 1)}\n')
    continuar = input('Deseja continuar? (S/N) \n')
    continuar = continuar.upper()
    if continuar == 'N':
        break

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





