#Ler 2 valores e mostrar um menu na tela, o programa deverá realizar a opção solicitada pelo usuário.

from time import sleep
v1 = int(input('Digite o 1° valor: '))
v2 = int(input('Digite o 2° valor: '))
op = 0
while op != 5:
    print('''    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NÚMEROS
    [ 5 ] SAIR DO PROGRAMA''')
    op = int(input('>>>>>>>Qual é a sua opção? '))
    if op == 1 :
        soma = v1 + v2
        print('A soma entre {} + {} é {}'.format(v1, v2, soma))
    elif op == 2:
        mult = v1 * v2
        print('A multiplicação entre {} x {} é {}'.format(v1, v2, mult))
    elif op == 3:
        if v1 > v2:
            maior = v1
        else:
            maior = v2
        print('Entre {} e {}  o maior valor é {}'.format(v1, v2, maior))
    elif op == 4:
        print('Informe os numeros novamente')
        v1 = int(input('Digite o 1° valor: '))
        v2 = int(input('Digite o 2° valor: '))
    elif op == 5:
        print('Finalizando...')
    else:
        print('Opção inválida, tente novamente')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa, volte sempre!!!')
