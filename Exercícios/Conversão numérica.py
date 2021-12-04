#Conversão de um número para binário, octal, hexadecimal

num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para fazer a conversão
[ 1 ] Converter para Binário
[ 2 ] Converte para Octal
[ 3 ] Converter para Hexadecimal''')

opção = int(input('Sua Opção: '))

if opção ==1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif opção ==2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opção ==3:
    print('{} convertido para HEXADECINAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção Inválida tente novamente')
