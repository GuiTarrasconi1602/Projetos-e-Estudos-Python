def somaPositivos(x, y):
    if x > 0 and y > 0:
        return x + y
    else:
        return -1


def divide(x, y):
    if y == 0:
        print('Erro não é possível fazer divisão por 0')
        return 0
    else:
        return x / y


def verificaTriangulo(x, y, z):
    if x == y == z:
        return 'Triângulo Equilátero'
    elif x == y or x == z or y == z:
        return 'Triângulo Isósceles'
    else:
        return 'Triãngulo Escalêno'


def verificaIdade(x):
    if x < 0:
        return "erro, menor que zero"
    elif x <= 12:
        return "criança"
    elif x <= 18:
        return "adolescente"
    elif x <= 120:
        return "adulto"
    else:
        return "erro, maior que 120"


def sinaleira(x):
    if x == 'Verde':
        print('Aberta')
    elif x == 'Amarelo' or x == 'Amarela':
        print('Atenção')
    elif x == 'Vermelho' or x == 'Vermelha':
        print('Fechada')
    else:
        print('Erro, cor inválida')


def contador(x):
    for n in range(x, 300):
        print(n)


def verificaPrimo(x):
    isPrimo = True
    cont = 2
    while cont < x:
        if x % cont == 0:
            isPrimo = False
            break
        cont += 1
    if isPrimo is False:
        return False
    else:
        return True


def achaMaior(x, y, z):
    if x >= y and x >= z:
        print(x)
    elif y >= x and y >= z:
        print(y)
    else:
        print(z)


def imprimePares(x):
    for n in range(0, x + 1, 2):
        print(n)


while True:
    print('\n''Escolha o número da opção desejada:''\n'
          '1. soma positivos''\n'
          '2. divide''\n'
          '3. verifica triângulo''\n'
          '4. verifica idade''\n'
          '5. sinaleira''\n'
          '6. conta até 300''\n'
          '7. verifica primo''\n'
          '8. acha maior''\n'
          '9. imprime pares''\n''\n'
          'Digite o número da opção desejada: ')
    opcao = int(input())
    if opcao == 1:
        num1 = int(input('Digite o primeiro valor: '))
        num2 = int(input('Digite o segundo valor: '))
        print(somaPositivos(num1, num2))
    elif opcao == 2:
        num1 = int(input('Digite o primeiro valor: '))
        num2 = int(input('Digite o segundo valor: '))
        print(divide(num1, num2))
    elif opcao == 3:
        num1 = input('Digite o comprimento do primeiro lado: ')
        num2 = input('Digite o comprimento do segundo lado: ')
        num3 = input('Digite o comprimento do terceiro lado: ')
        print(verificaTriangulo(num1, num2, num3))
    elif opcao == 4:
        num = int(input('Digite a idade: '))
        print(verificaIdade(num))
    elif opcao == 5:
        cor = input('Digite a cor do sinal: ')
        corfinal = cor.title()
        sinaleira(corfinal)
    elif opcao == 6:
        num = int(input('Digite um valor: '))
        contador(num)
    elif opcao == 7:
        num = int(input('Digite um número: '))
        numero = verificaPrimo(num)
        if numero is False:
            print('Não é primo!')
        else:
            print('É primo!')
    elif opcao == 8:
        num1 = int(input('Digite o primeiro valor: '))
        num2 = int(input('Digite o segundo valor: '))
        num3 = int(input('Digite o terceiro valor: '))
        achaMaior(num1, num2, num3)
    elif opcao == 9:
        num = int(input('Digite um valor: '))
        imprimePares(num)
    else:
        break





