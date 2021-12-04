#LEIA UM ÂNGULO QUALQUER E MOSTRE O VALOR DO SENO, COSSENO E TANGENTE


import math
an = float(input('Digite o ângulo:'))
seno = math.sin(math.radians(an))
print ('O ângulo de {} tem o seno de {:.2f}'.format(an, seno))
cos = math.cos(math.radians(an))
print('O ângilo de {} te o cosseno de {:.2f}'.format(an, cos))
tan = math.tan(math.radians(an))
print('O ângilo de {} te a tangente de {:.2f}'.format(an, tan))
