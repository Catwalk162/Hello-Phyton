from random import randint
num = randint(0,5)

users = int(input('Digite um valor entre 0 e 5: '))

print('Venceu!'if users == num else 'Perdeu!')
c = input('pressione Enter para fechar!')