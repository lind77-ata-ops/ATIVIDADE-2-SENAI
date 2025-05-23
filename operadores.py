# SISTEMA DE MEDIA DE NOTAS


print('SEJA BEM VINDO(A) AO SISTEMA DE NOTAS')
nome = input('Digite o nome do aluno: ')

nota_mat = float(input('Digite a nota de matematica: '))
nota_port = float(input('Digite a nota de portugues: '))
nota_ing =  float(input('Digite a nota de ingles: '))

media = (nota_mat + nota_port + nota_ing) / 3

print('O(A) aluno(a)', nome, 'esta com a media', media)

aprovado  = media >= 7
reprovado  = media < 5
recuperação  = media >=5 and media <7

print(f'''
O(a) aluno(a) {nome}
APROVADO - {aprovado}
REPROVADO - {reprovado}
RECUPERAÇÃO - {recuperação}
''')