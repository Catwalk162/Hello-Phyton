nome = str(input('Digite seu nome completo: '))

s = nome.split()
t = len(s) - 1 # Ou s[-1]

print('Primeiro = {}'.format(s[0]))
print('Último = {}'.format(s[t]))
c = input('pressione Enter para fechar!')