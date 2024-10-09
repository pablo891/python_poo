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


# Passo 5 - Criando comando SQL para inserir os dados na tabela
sql = 'SELECT * FROM funcionario'


# Passo 6 - Executar o comando sql e substituir o '?' pelos campos
consulta.execute(sql)

# Passo 7 - Exibir dados da tabela
resultado = consulta.fetchall() #irá trazer todos os registros que existem na tabela do banco de dados

for itens in resultado:
    print(f'Código: {itens[0]} Nome: {itens[1]} Salário: R${itens[2]} Cargo: {itens[3]}')
# Passo 8 - encerrar a conexão
conexao.close()
