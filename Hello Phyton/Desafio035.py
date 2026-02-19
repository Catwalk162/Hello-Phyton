reta0 = float(input('Digite um comprimento: '))
reta1 = float(input('Digite outro comprimento: '))
reta2 = float(input('Digite outro comprimento: '))

if (reta0 < (reta1 + reta2)) and (reta1 < (reta0 + reta2)) and (reta2 < (reta1 + reta0)):
    print('Pode formar um triângulo!')
else:
    print('Não pode formar um triângulo!')
c = input('pressione Enter para fechar!')