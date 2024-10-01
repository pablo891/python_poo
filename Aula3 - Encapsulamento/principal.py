from conta import Conta

minhaConta = Conta(321, 'Epamenondas Soares', 2000)

minhaConta.relatorio()

minhaConta.setLimite(8000)
minhaConta.relatorio()

print(f'Seu limite atual é {minhaConta.getLimite()}')

minhaConta.depositar(100)
minhaConta.relatorio()

minhaConta.sacar(150)
minhaConta.relatorio()