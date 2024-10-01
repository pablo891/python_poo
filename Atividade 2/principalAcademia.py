from academia import Aluno

print('ACADEMIA SÃO LUÍS')
listaAluno = []

for contador in range(2):
    nome = input('Informe seu nome: ')
    idade = int(input('Informe sua idade: '))
    peso = float(input('Informe seu peso: '))
    altura = float(input('Informe sua altura: '))


    aluno = Aluno(nome, idade, peso, altura)
    listaAluno.append(Aluno)

listaAluno(0).exibirDados()
listaAluno(0).calcularIMC()

listaAluno(1).exibirDados()
listaAluno(1).calcularIMC()