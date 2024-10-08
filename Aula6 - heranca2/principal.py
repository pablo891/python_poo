from pessoa import Pessoa, Aluno, Professor

pessoa1 = Pessoa('Pablo', 18)
aluno1 = Aluno('Thaynara', 17, 903)
pf1 = Professor('Irineu', 38, 'Física')

pessoa1.info()

aluno1.info()
aluno1.estudar()

pf1.ensinar()