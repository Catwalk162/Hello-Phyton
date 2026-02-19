km = float(input('Digite a quatidade de quilômetros do carro alugado: '))
dias = int(input('Por quantos dias o carro foi alugado? '))

preco = 60*dias + 0.15*km

print('Com {} dias e {:.2f}km o valor ficou {:.2f}R$'.format(dias,km,preco))
c = input('pressione Enter para fechar!')