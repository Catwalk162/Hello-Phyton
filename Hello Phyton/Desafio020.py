from random import shuffle
nome1 = str(input('Digite o nome do primeiro aluno: '))
nome2 = str(input('Digite o nome do segundo aluno: '))
nome3 = str(input('Digite o nome do terceiro aluno: '))
nome4 = str(input('Digite o nome do quarto aluno: '))

nomes = [nome1,nome2,nome3,nome4]

shuffle(nomes)

print('Primeiro vai ser o grupo de {}, segundo grupo é o de {}, terceiro é o de {} e por último o quarto mas não menos importante {}!'.format(nomes[0], nomes[1],nomes[2],nomes[3]))
c = input('pressione Enter para fechar!')