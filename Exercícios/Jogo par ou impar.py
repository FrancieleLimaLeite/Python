#Jogue par ou ímpar com o computador, o jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas conquistadasno final do jogo


from random import randint
vitoria = 0
print('-=' * 30)
print('Jogo do PAR ou IMPAR')
print('-=' * 30)
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 11)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = str(input('Par ou Impar?[P/I]: ')).upper().strip()[0]
    print(f'Você jogou {jogador}, e o computador jogou {computador}. Total deu {total}')
    print('Deu PAR' if total % 2 == 0 else 'Deu IMPAR' )
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            vitoria += 1
        else:
            print('Você perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você venceu!!!')
        else:
            print('Você perdeu')
            break
    print('Vamos jogar novamente...')
print(f'Você venceu {vitoria} vezes.')

