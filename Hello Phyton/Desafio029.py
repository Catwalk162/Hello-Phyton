velocidadecar = float(input('Digite a velocidade do carro em km: '))
preco = 7*(velocidadecar - 80)
print('Você foi multado em {:.2f}R$!'.format(preco)if velocidadecar > 80 else 'Você não foi multado!')
c = input('pressione Enter para fechar!')