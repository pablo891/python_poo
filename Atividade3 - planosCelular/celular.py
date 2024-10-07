class Celular:
    def __init__(self, numero, plano, duracao, saldo = 0):
        self.__numero = numero
        self.__plano = plano
        self.__duracao = duracao
        self.__saldo = saldo

    # Métodos
    @property
    def plano(self):
        return self.__plano
   
    @plano.setter
    def plano (self, tipo):
        self.__plano = tipo  

    def recarregarValor(self, valor):
        if self.__plano == 'pré-pago':
            self.__saldo += valor
        elif self.plano == 'pós-pago':
            self.__saldo == self.__saldo
        
    def fazerChamada(self, duracao):
        if self.__saldo < 0:
            print('Erro ao realizar chamada. Você não tem saldo')
        
        elif self.__plano == 'pós-pago':
            print('Não é possível fazer recargas em plans pós-pagos')         
            print('O valor total será cobrado ao final do mês')
        else:
            valorMinuto = 1.50
            self.__saldo -= (duracao * valorMinuto)
        
    
    def exibirDados(self):
        print('-' * 100)
        print(f'Número: {self.__numero}\nPlano: {self.__plano}\nSaldo atual: R${self.__saldo}')