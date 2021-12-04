#Tupla com nome de produtos e seus respectivos preços. Mostrar uma listagem de preços organizando os dados em forma tabular

listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Trasferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livros', 34.90)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for posição in range(0, len(listagem)):
    if posição % 2 == 0:
        print(f'{listagem[posição]:.<30}', end='')
    else:
        print(f'R${listagem[posição]:>7.2f}')
print('-' * 40)
