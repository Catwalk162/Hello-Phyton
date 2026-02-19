salario = float(input('Qual o seu salário? '))

if salario >= 1250:
    novosalario = salario*1.10
    print('Com seu aumento ficou {:.2f}R$'.format(novosalario))
else:
    novosalario = salario*1.15
    print('Com seu aumento ficou {:.2f}R$'.format(novosalario))
c = input('pressione Enter para fechar!')