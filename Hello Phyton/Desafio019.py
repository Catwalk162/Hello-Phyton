from random import choice, choices
nome1 = str(input('Digite o nome do primeiro aluno: '))
nome2 = str(input('Digite o nome do segundo aluno: '))
nome3 = str(input('Digite o nome do terceiro aluno: '))
nome4 = str(input('Digite o nome do quarto aluno: '))

nomes = [nome1,nome2,nome3,nome4]

sorteado = choice(nomes)

print('O sorteado foi {}!'.format(sorteado))
c = input('pressione Enter para fechar!')