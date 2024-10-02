class Calculadora:
    def __init__(self, num1, num2):
        self.__num1 = num1
        self.__num2 = num2
    
    def somar(self):
        soma = self.__num1 + self.__num2
        print(f'Soma dos valores: {soma}')
    
    def subtrair(self):
        subtracao = self.__num1 - self.__num2
        print(f'Subtração dos valores: {subtracao}')

    def multiplicar(self):
        mult = self.__num1 * self.__num2
        print(f'Multiplicação dos valores: {mult}')

    def dividir(self):
        divisao = self.__num1 / self.__num2
        print(f'Divisão dos valores: {divisao:.2f}')
    
    def potencia(self):
        if self.__num1 > self.__num2:
            potencia = self.__num1 ** self.__num2
            print(f'Potenciação dos valores: {potencia:.2f}')
    
    def verificarParImpar(self, valor):
        if valor % 2 == 0:
            print('O valor informado é par')
        else:
            print('O valor informado é ímpar')