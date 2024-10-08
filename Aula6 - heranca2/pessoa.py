class Pessoa: # superclasse ou classe mãe
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    def info(self):
        print(f'Nome: {self._nome}\nIdade: {self._idade}')

# Classe filha 1 - Aluno
class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade) # Utilizando o construtor da classe mãe
        self._matricula = matricula # Estamos utilizando um atributo exclusivo da classe filha

    def estudar(self):
        print(f'{self._nome}: está matriculado com o código: {self._matricula} e continua estudando normalmente')

# Classe filha 2 - Professor
class Professor(Pessoa):
    def __init__(self, nome, idade, disciplina):
        super().__init__(nome, idade)
        self._disciplina = disciplina

    def ensinar(self):
        print(f'{self._nome}, professor(a) da disciplina {self._disciplina}, está ensinando')