# Estamo acessando o arquivo 'pessoa' e dentro desse arquivo estamos importando a classe 'Pessoa'
from pessoa import Pessoa

# Criando objetos
p1 = Pessoa('Joana', 'Correr', 'Rua dos alfinetes, 2121')
p1.exibirHobby()
p1.alterarHobby('Natação')

# Solicitando dados do usuário
nomePessoa = input('Informe o nome da pessoa: ')
hobbyPessoa = input('Informe o hobby da pessoa: ')
endPessoa = input('Qual o endereço? ')

p2 = Pessoa(nomePessoa, hobbyPessoa, endPessoa)
p2.exibirHobby()