nome = str(input('Digite seu nome: '))

u = nome.upper()

l = nome.lower()

s = nome.split()

c = nome.count(' ')

d = len(nome) - c
z = len(nome.replace(' ',''))
k = len(s[0])

print('O nome em maiúsculo é {}'.format(u))

print('O nome em minúsculo é {}'.format(l))

print('O nome inteiro tem um total de {} letras'.format(z)) # Ou d

print('O primeiro nome tem um total de {} letras'.format(k))
c = input('pressione Enter para fechar!')

