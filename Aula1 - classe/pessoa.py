class Pessoa:
    # Atributos
    nome = "Fulano"
    peso = "71kg"
    escolaridade = "Ensino Médio"

    # Métodos
    def falar(self, texto):
        print(f'Tenho algo para te dizer: {texto}')

# Criando os objetos
pessoa1 = Pessoa()

print(pessoa1.nome)
pessoa1.falar('Boa tarde! Hoje é segunda-feira')