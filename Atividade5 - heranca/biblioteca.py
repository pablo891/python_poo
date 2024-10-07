import datetime

class Biblioteca:
    def __init__(self, titulo, autor, anoPublicacao, numeroPagina):
        self._titulo = titulo
        self._autor = autor
        self._anoPublicacao = anoPublicacao
        self._numeroPagina = numeroPagina
    
    def detalhes(self):
        print(f'Informações do item: \nTítulo: {self._titulo}\nAutor: {self._autor}\nAno de Publicação: {self._anoPublicacao}\nNúmero de páginas: {self._numeroPagina}')
    
    def calcularIdadeItem(self):
        ano = datetime.datetime.now()
        idade = ano.year - self._anoPublicacao

        if idade > 70:
            print(f'O item é considerado muito antigo, com {idade} anos de idade')
    
        elif idade >= 30 and idade <= 70:
            print(f'O item é considerado recente, com {idade} anos de idade')
        
        elif idade < 30:
            print(f'O item é considerado contemporâneo, com {idade} anos de idade')
        
        elif idade < 0:
            print('Idade inválida')
        print(f'Item: {self._titulo}\nAno: {self._anoPublicacao} \nIdade: {idade} anos')


class Livro(Biblioteca):
    def verificarTamanho(self):
        if self._numeroPagina >= 300:
            print('O livro contém mais de 300 páginas, e é longo')
        
        elif self._numeroPagina < 300:
            print('O livro contém menos de 300 páginas, e é curto')

class Revista(Biblioteca):
    def verificarEdicao(self):
        self._autor = 'Desconhecido'
        if self._anoPublicacao >= 26:
            print(f'A revista {self._titulo}, de {self._anoPublicacao} é uma edição ESPECIAL')
        elif self._anoPublicacao > 0 and self._anoPublicacao < 26:
            print(f'A revista {self._titulo}, de {self._anoPublicacao} é uma edição simples')