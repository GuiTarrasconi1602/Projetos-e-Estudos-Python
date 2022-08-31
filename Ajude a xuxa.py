print('Digite o número de patinhos que você quer na música "5 Patinhos" da Xuxa.''\n'
      '(Obs: Somente números positivos maiores ou iguais a 2)''\n')
patos = int(input('Digite o número de patinhos: '))
patosInicial = patos
while patos < 2:
    patos = int(input('Digite o número de patinhos: '))
    patosInicial = patos
print('\n')
while patos > 3:
    print(f'{patos} patinhos''\n'
          f'Foram passear ' '\n'
          f'Além das montanhas' '\n'
          f'Para brincar' '\n'
          f'A mamãe gritou''\n'
          f'Quack quack quack ' '\n'
          f'Mas só {patos - 1} patinhos ''\n'
          f'Voltaram de lá' '\n')
    patos -= 1


if patos == 3:
    print(f'{patos} patinhos''\n'
          f'Foram passear ' '\n'
          f'Além das montanhas' '\n'
          f'Para brincar' '\n'
          f'A mamãe gritou''\n'
          f'Quack quack quack ' '\n'
          f'Mas só {patos - 1} patinhos ''\n'
          f'Voltaram de lá' '\n')
    patos = patos - 1

if patos == 2:
    print(f'{patos} patinhos''\n'
          f'Foram passear ' '\n'
          f'Além das montanhas' '\n'
          f'Para brincar' '\n'
          f'A mamãe gritou''\n'
          f'Quack quack quack ' '\n'
          f'Mas só {patos - 1} patinho ''\n'
          f'Voltou de lá' '\n')
    patos = patos - 1
if patos == 1:
    print(f'{patos} patinho foi passear''\n'
          f'Além das montanhas''\n'
          f'Para brincar''\n'
          f'A mamãe gritou''\n'
          f'Quack quack quack''\n'
          f'Mas nenhum patinho''\n'
          f'Voltou de lá''\n''\n'
          f'A mamãe patinha''\n'
          f'Foi procurar''\n'
          f'Além das montanhas''\n'
          f'Na beira do mar''\n'
          f'A mamãe gritou''\n'
          f'Quack quack quack''\n'
          f'E os {patosInicial} patinhos''\n'
          f'Voltaram de lá''\n')


