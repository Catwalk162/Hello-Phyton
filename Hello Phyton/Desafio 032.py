ano = int(input('Digite um ano qualquer: '))
resto0 = ano%4
resto1 = ano%400
resto2 = ano%100

if (resto0 == 0 and resto2 != 0) or (resto1 == 0):
    print('O ano é bissexto!')
else:
    print('O ano não é bissexto!')
c = input('pressione Enter para fechar!')