#LEIA O COMPRIMENTO DO CATETO OPOSTO E O ADJACENTEDE UM TRIÂNGULO RETÂNGULO, CALCULE E MOSTRE O COMPRIMENTO DA HIPOTENUSA





#modelo1
#ca = float(input('Digite o valor do Cateto Adjacente:'))
#co = float(input('Digite o valor do Cateto Oposto:'))
#h = (ca**2+co**2)** (1/2)

#print ('O valor da Hipotenusa é: {:.2f}'.format(h))

#Com Função Math do python
import math
ca = float(input('Digite o valor do Cateto Adjacente:'))
co = float(input('Digite o valor do Cateto Oposto:'))
h = math.hypot(co, ca)
print ('O valor da Hipotenusa é: {:.2f}'.format(h))
