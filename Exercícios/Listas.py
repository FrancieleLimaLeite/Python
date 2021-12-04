#ler nome e peso de várias pessoas e guardar em  uma lista, depois mostrar, quantas pessoas foram cadastradas, uma lista com as pessoas mais pesadas, e uma lista com as pessoas mais leves

dados = []
pessoas = []
maiorpeso = menor = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(dados) == 0:
        maiorpeso = menor = dados[1]
    else:
        if dados[1] > maiorpeso:
            maiorpeso = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    r = str(input('Quer continuar?: '))
    if r in 'Nn':
        break

print(f'Ao todo foram {len(pessoas)} cadastros')
print(f'Os maiores pesos foram {maiorpeso}', end='')
for p in pessoas:
    if p[1] == maiorpeso:
        print(f'[{p[0]}]', end='')
print()
print(f'Os menores pesos foram {menor}', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}]', end='')
print()
