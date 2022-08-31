"""
print('Digite o nome de 13 pessoas!')
i = 0
nomes = []
while i < 13:
    nome = input(f'Digite o {i + 1}o nome: ')
    nomes.append(nome)
    i = i + 1

for n in nomes:
    print(n)
"""
"""

i = 0
while i < 1000:
    i += 1
    print(i)
"""
"""

i = 0
pares = int
while i < 200:
    if i % 2 == 0:
        print(i)
    i += 1
"""
"""

i = 1000
while i > 0:
    print(i)
    i = i - 1
"""
"""

i = 0
inter = 0
gremio = 0
outros = 0
while i < 10:
    nomes = input('Digite o seu time: ')
    if nomes == 'inter':
        inter += 1
    elif nomes == 'gremio':
        gremio += 1
    else:
        outros += 1
    i += 1
print(f'O número de torcedores do inter é: {inter}')
print(f'O número de torcedores do gremio é: {gremio} ')
print(f'O número de torcedores dos outros times é: {outros}')
"""
"""

lista = []
i = 0
while i < 4:
    numeros = int(input(f'Digite o {i + 1}o numero: '))
    lista.append(numeros)
    i += 1
print(lista)
"""
"""
i = 0
quant = int(input('Quantos números? '))
while i < quant:
    num = int(input(f'Digite o {i + 1}o número: '))
    if num > 0:
        print('Positvo.')
    elif num < 0:
        print('Negativo')
    else:
        print('Zero')
    i += 1
"""
"""

print('Digite dois valores!')
num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))

if num1 < num2:
    print('Os números pares entre os dois números são:')
    while num1 < num2:
        if num1 % 2 == 0:
            print(num1)
        num1 += 1
elif num2 < num1:
    print('Os números pares entre os dois números são:')
    while num2 < num1:
        if num2 % 2 == 0:
            print(num2)
        num2 += 1
else:
    print('Os dois valores são iguais')
"""
"""
i = 0
soma = 0
while i <= 198:
    soma += i
    i += 1
print(soma)
"""
"""

cont = 0
while True:
    num = int(input('Digite um número: '))
    if num < 0:
        print('Número negativo')
    elif num == 0:
        print('Número digitado foi o zero!')
    else:
        print('Número Postivo!')
    cont += 1
    if cont == 10:
        break
    
"""

