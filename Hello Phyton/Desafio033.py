num0 = float(input('Digite um número: '))
num1 = float(input('Digite outro número: '))
num2 = float(input('Digite outro número: '))

if num0 > num1 and num0 > num2:
    print('O maior valor é {} !'.format(num0))
elif num1 > num0 and num1 > num2:
    print('O maior valor é {} !'.format(num1))
else:
    print('O maior valor é {} !'.format(num2))

if num0 < num1 and num0 < num2:
    print('O menor valor é {} !'.format(num0))
elif num1 < num0 and num1 < num2:
    print('O menor valor é {} !'.format(num1))
else:
    print('O menor valor é {} !'.format(num2))
c = input('pressione Enter para fechar!')