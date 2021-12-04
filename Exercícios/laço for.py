#Ler seis números inteiros e mostrar a soma apenas daqueles que forem pares, se o valor digitado for ímpar, desconsiderar.

soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o {}º numero: '.format(c)))
    if num % 2 == 0:
         soma = soma + num
         cont += 1
print('Você informou {} numeros pares e a soma é {}'.format(cont, soma))


