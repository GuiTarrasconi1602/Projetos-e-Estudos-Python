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