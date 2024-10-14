import sqlite3
class Funcionario:
    def conexao(self):
        conexao = sqlite3.connect('departamento.db')
        consulta = conexao.cursor()
        tabela = '''
        CREATE TABLE IF NOT EXISTS funcionario(
        codigo INTEGER PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(100),
        salario FLOAT,
        cargo VARCHAR(100)
        );
        ''' 
        consulta.execute(tabela)
        return conexao
    
    def inserir(self, nome, salario, cargo):
        conexao = self.conexao() # estamos chamando o método que irá conectar ao banco, esse método foi criado mais acima

        sql = 'INSERT INTO funcionario VALUES (?,?,?,?)'

        campos = (None, nome, salario, cargo)

        consulta = conexao.cursor()
        consulta.execute(sql, campos)

        conexao.commit()

        print(consulta.rowcount, ' linha(s) inseridas com sucesso')

        conexao.close()

    def consultar(self):
        conexao = self.conexao()
        consulta = conexao.cursor()

        sql = 'SELECT * FROM funcionario'
        consulta.execute(sql)

        resultado = consulta.fetchall()

        for itens in resultado:
            print(f'Código: {itens[0]}')
            print(f'Nome: {itens[1]}')
            print(f'Salário: {itens[2]}')
            print(f'Cargo: {itens[3]}')
            print('-' * 40)