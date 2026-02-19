from math import cos, sin, tan, radians
theta = float(input('Digite um ângulo qualquer: '))
rad = radians(theta)
tangente = tan(rad)
cosseno = cos(rad)
seno = sin(rad)

print('O seno tem valor {}, o cosseno tem valor {} e a tangente tem valor {}'.format(seno, cosseno, tangente))
c = input('pressione Enter para fechar!')