numero = str(input('Digite um valor qualquer de 0 a 9999: '))

numero = numero.zfill(4)
print('Unidade: {}'.format(numero[3]))
print('Dezena: {}'.format(numero[2]))
print('Centena: {}'.format(numero[1]))
print('Milhar: {}'.format(numero[0]))
c = input('pressione Enter para fechar!')