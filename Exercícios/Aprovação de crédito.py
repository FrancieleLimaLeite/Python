#APROVAÇÃO DE EMPRÉSTIMO BANCÁRIO PARA COMPRA DE UMA CASA.



print('\033[7m Seja bem vindo ao sistema de simulação de empréstimo!\033[m')
vc = float(input('Qual o é o valor da casa que deseja comprar? R$: '))
sl = float(input('Qual é seu salário bruto? R$: '))
an = int(input('Em quantos anos irá pagar? R:'))

prestação = vc/(an *12)
min = sl * 30/100

print('Para pagar a casa de R${:.2f} em {} anos'.format(vc,an), end='')
print(' a prestação será de R${:.2f}'.format(prestação))
if prestação <= min:
    print('Empréstimo pode ser CONCEDIDO')
else:
    print('Empréstimo NEGADO')
