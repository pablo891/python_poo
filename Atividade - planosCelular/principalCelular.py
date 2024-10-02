from celular import Celular

print('INFORMAÇÕES DO CLIENTE 1:')
cliente1 = Celular('(98) 97312-3213', 'pré-pago', 10)
cliente1.exibirDados()
cliente1.recarregarValor(50)
cliente1.fazerChamada(10)
cliente1.exibirDados()
print('\n' * 2)

print('INFORMAÇÕES DO CLIENTE 2:')
cliente2 = Celular('(71) 98312-3182','pós-pago', 5)
cliente2.exibirDados()
cliente2.recarregarValor(30)
cliente2.fazerChamada(5)
cliente2.exibirDados()