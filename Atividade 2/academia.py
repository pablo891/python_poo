class Aluno:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
    
    # Métodos
    def exibirDados (self):
        print('-' * 60)
        print(f'Nome do Aluno: {self.nome}\nIdade: {self.idade} anos\nPeso: {self.peso}kg\nAltura: {self.altura}m')
    
    def calcularIMC (self):
        imc = self.peso / (self.altura * self.altura)
        print(f'Índice de massa corporal (IMC): {imc:.2f}')
