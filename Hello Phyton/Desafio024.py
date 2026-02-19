cidade = str(input('Digite um nome de uma cidade: '))

cidade = cidade.upper().split()

c = 'SANTO' in cidade[0]
print('{}'.format(c))
c = input('pressione Enter para fechar!')