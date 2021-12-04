#Ler preço de vários produtos e mostrar o total gasto, quantos produtos custam mais de mil reais e qual o nome do produto mais barato.

totgasto = 0
maisdemil = 0
maisbarato = 0
cont = 0
barato = ' '
print('-=' * 30)
print('BEM VINDO (A) Á LOJA DA FRANCIELE')
print('-=' * 30)
while True:
    nomep = str(input('Nome do produto: '))
    preço = float(input('Valor do produto: R$ '))
    cont += 1
    totgasto += preço
    if preço > 1000:
        maisdemil += 1
    if cont == 1 or preço < maisbarato:
        maisbarato = preço
        barato = nomep
    resp = ' '
    while resp not in 'SN':
         resp = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    if resp in 'Nn':
        break
print('{:-^40}'.format('FIM DO PROGRAMA!'))
print(f'O total da compra foi R${totgasto:.2f}')
print(f'Temos {maisdemil} produtos que custam mais de R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${maisbarato:.2f}')

