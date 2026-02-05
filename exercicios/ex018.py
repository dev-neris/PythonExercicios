import math
from math import sin, cos, tan, radians
angulo = float(input('Digite o Ângulo que você deseja:'))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print('O ângulo de {} tem o COSSENO de {:.2f}, o seno de {:.2f} e a tangente de {:.2f}'.format(angulo, seno, cosseno, tangente))