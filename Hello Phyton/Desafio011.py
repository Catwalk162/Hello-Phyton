largura = float(input('Qual a largura da sua parede em metros?  '))
altura = float(input('Qual a altura da sua parede em metros? '))

aquadrada = largura*altura
tinta = aquadrada/2

print('A quantidade de tinta necessária é {:.3} litros'.format(tinta))
c = input('pressione Enter para fechar!')