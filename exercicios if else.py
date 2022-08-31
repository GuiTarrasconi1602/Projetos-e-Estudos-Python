# EXERCÍCIO 1
"""
numero = int(input('Escreva um número inteiro: '))
if numero % 2 == 0:
    print(f'O número {numero} é PAR.')
else:
    print(f'O número {numero} é IMPAR.')
"""
# EXERCÍCIO 2
"""
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

if num1 > num2:
    print(num1)
elif num1 < num2:
    print(num2)
else:
    print(f'Os números são iguais, o número é {num1}')
"""
# EXERCÍCIO 3
"""
num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

if num2 != 0:
    print(f'A divisão do número {num1} pelo número {num2} é: {int(num1/num2)}')
else:
    print('Impossível fazer uma divisão por 0')
"""
# EXERCÍCIO 4
"""

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))

if num2 > num1 < num3:
    print(f'O menor número é {num1}.')
elif num1 > num2 < num3:
    print(f'O menor número é {num2}.')
else:
    print(f'O menor número é {num3}.')
"""
# EXERCÍCIO 5
"""
preco = float(input('Digite o valor de um caderno: '))

if preco < 0:
    print('Preço inválido')
elif preco < 30.0:
    print('Preço baixo')
elif preco < 50.0:
    print('Preço médio')
else:
    print('Preço alto')
"""
# EXERCÍCIO 6
"""

numero = float(input('Digite um valor: '))\

if numero < 100:
    final = numero + (numero * 0.1)
elif 100 <= numero < 300:
    final = numero + (numero * 0.2)
elif 300 <= numero < 1000:
    final = numero + (numero * 0.5)
elif numero < 0:
    print('Valor negativo inválido!')
print(f'O valor inserido com o imposto é : {final}')
"""
# EXERCÍCIO 7
"""

ano = int(input('Digite um ano: '))

if ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 0:
    print(f'O ano {ano} é bissexto')
else:
    print(f'O ano {ano} não é bissexto')
"""
# EXERCÍCIO 8
"""
print('Digite 1 para somar dois valores' '\n'
      'Digite 2 para subtrair dois valores' '\n'
      'Digite 3 para multiplicar dois valores' '\n'
      'Digite 4 para dividir dois valores' '\n'
      'Digite 5 para realizar uma potência entre dois valores' '\n'
      'Digite 6 para realizar uma radiciação entre dois valores' '\n'
      'Digite qualquer outro número para sair')
numero = int(input('Digite o número: '))
if numero == 1:
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))
    print(f'A soma dos valores é: {num1 + num2}')

elif numero == 2:
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))
    print(f'A subtração dos valores é: {num1 - num2}')

elif numero == 3:
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))
    print(f'A multiplicação dos valores é: {num1 * num2} ')

elif numero == 4:
    
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))
    if num2 != 0
        print(f'A divisão dos valore é: {num1 / num2}')
    else:
        print('Não posso dividir por 0')
elif numero == 5:
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))
    print(f'A potenciação dos valores é {num1 ** num2}')


elif numero == 6:
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))
    print(f'A radiciação dos valores é: {num1 ** (1/num2)}')

else:
    print('Saindo...')
"""
# EXERCÍCIO 9
"""
def calculo_nota(nota1, nota2):
    return (nota1 * 0.33) + (nota2 * 0.67)


nota1 = float(input('Digite a nota do Grau A: '))
nota2 = float(input('Digite a nota do Grau B: '))
if nota1 < 0 or nota2 < 0:
    print('Nota negativa impossível fazer o cálculo, digite uma nota válida!')
else:
    final = calculo_nota(nota1, nota2)
    if final < 6:
        print('Você precisará fazer o Grau C')
    elif final > 6:
        print('Você não precisará fazer o Grau C')
"""
# EXERCÍCIO 10
"""
letra = str(input('Digite uma letra: '))
letra = letra.upper()
if letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U':
    print(f'A letra {letra} é uma VOGAL.')
else:
    print(f'A letra {letra} é uma consoante.')
"""
