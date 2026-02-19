from math import sqrt, pow
catetooposto = float(input('Digite o cateto oposto: '))
catetoadjacente = float(input('Digite o cateto adjacente: '))

hipotenusa = sqrt(pow(catetooposto,2) + pow(catetoadjacente,2))

print('O triângulo com CO {} e CA {} tem hipotenusa de tamanho {}'.format(catetooposto,catetoadjacente,hipotenusa))
c = input('pressione Enter para fechar!')
