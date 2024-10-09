import sqlite3

# Passo 1 - Conexã com o banco
conexao = sqlite3.connect('departamento.db')

# Passo 2 - Verificar se a tabela existe ou não
tabela = '''
CREATE TABLE IF NOT EXISTS funcionario(
    codigo INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(100),
    salario FLOAT,
    cargo VARCHAR(100)
);
'''

# Passo 3 - Acessar o objeto cursor() da biblioteca sqlite3, para manipular dados do banco
consulta = conexao.cursor()

# Passo 4 - Executar o comando da criação da tabela
consulta.execute(tabela)

# Passo 5 - solicitar dados do usuário
nome = input('Informe o nome do funcionário: ')
salario = float(input('Informe o salário do funcionário: '))
cargo = input('Informe o cargo do funcionário: ')

# Passo 6 - Criando comando SQL para inserir os dados na tabela
sql = 'INSERT INTO funcionario VALUES(?,?,?,?);' # Colocamos ? no lugar dos dados reais, para evitar possíveis ataques de sql injection. Isso é uma implementação da biblioteca sqlite3

# Passo 7 - Organizar os dados que irão substituir ? no comando sql
campos = (None, nome, salario, cargo) # Criando uma tupla com os dados que irão substituir ? ao informar o valor 'None', estamos dizendo que será atribuído o valor padrão do AUTOINCREMENT

# Passo 8 - Executar o comando sql e substituir o '?' pelos campos
consulta.execute(sql, campos)

# Passo 9 - Gravar os dados no Banco
conexao.commit()

print(consulta.rowcount, ' linha(s) inseridas com sucesso')

# Passo 10 - encerrar a conexão
conexao.close()
