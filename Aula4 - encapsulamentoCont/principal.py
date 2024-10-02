from funcionario import Funcionario

funcionario1 = Funcionario('Pablo', 3000)

print(f'Seu nome atual é: {funcionario1.getNome()}')

funcionario1.setNome('Thaynara')

print(f'Seu nome atual é {funcionario1.getNome()}')

# Estamos tentando acessar o atributo salário
print(f'Seu salário atual é: R${funcionario1.salario}')

funcionario1.salario = 5000

print(f'Seu salário atual é R${funcionario1.salario}')