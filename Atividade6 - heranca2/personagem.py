class Personagem:
    def __init__(self, nome, vida = 100, rank = ''):
        self._nome = nome
        self._vida = vida
        self._rank = rank

    def receberDano(self, dano):
        self._vida -= dano
        print(f'Você recebeu {dano} de dano')

    def verificarVida(self):
        if self._vida <= 0:
            print(f'O personagem {self._nome} morreu')
    
    def detalhes(self):
        print(f'PERSONAGEM: {self._nome} | VIDA: {self._vida}%')

    @property
    def vida(self):
        return self._vida

    @vida.setter
    def vida(self):
        return self._vida
    
class Heroi(Personagem):
    def __init__(self, nome, vida = 100, rank = '', identidadeSecreta = '', energia = 50):
        super().__init__(nome, vida, rank)
        self._identidadeSecreta = identidadeSecreta
        self._energia = energia
    
    def executarHabilidade(self, tipoHabilidade, energiaPoder):
        if self._energia > energiaPoder:
            self._energia -= energiaPoder
            print(f'Poder: {tipoHabilidade} | Energia consumida: {energiaPoder} | Energia Restante: {self._energia}')

        else:
            print('Não foi possível utilizar o poder')

    def recarregarEnergia(self, aumentoEnergia):
        self._energia += aumentoEnergia
        print(f'A energia atual é: {self._energia} %')
    
    def chamarAliado(self, nomeAliado, descricaoHabilidade):
        print(f'ALIADO: {nomeAliado}\nHABILIDADE: {descricaoHabilidade}')

class Vilao(Personagem):
    def __init__(self, nome, vida = 100, rank = '', malicia = 70 ):
        super().__init__(nome, vida, rank)
        self._malicia = malicia
    
    def desferirGolpe (self, tipoGolpe, consumoMalicia):
        if self._malicia > consumoMalicia:
            self._malicia -= consumoMalicia
            print(f'GOLPE: {tipoGolpe} | Malicia consumida: {consumoMalicia} | Malícia Restante: {self._malicia}')
    
    def planejarArmadilha(self, tipoArmadilha):
        print(f'O vilão está planejando a armadilha "{tipoArmadilha}"')
    
    def fugir(self, tipoFulga):
        print(f'O vilão conseguiu escapar usando a fuga: {tipoFulga}')