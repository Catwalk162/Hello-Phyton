distancia = float(input('Digite a distância da viagem em km: '))

preco200 = distancia*0.5
preco8 = distancia*0.45

print('O preço ficou {:.2f}R$'.format(preco200)if distancia > 200 else 'O preço ficou {}R$'.format(preco8))
c = input('pressione Enter para fechar!')