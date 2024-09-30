class Livro:
    def __init__(self, titulo, autor, anoPublicacao):
        self.titulo = titulo
        self.autor = autor
        self.anoPublicacao = anoPublicacao
    
    # Métodos
    def exibirInformacoes (self):
        print(f'Título do livro: {self.titulo}\nAutor: {self.autor}\nAno de Publicação: {self.anoPublicacao}')
    
    def vericarIdadeLivro (self):
        anoReal = 2024 - self.anoPublicacao
        if anoReal >= 50:
            print(f'O livro {self.titulo} é um clássico!')
        else:
            print(f'O livro {self.titulo} ainda não é considerado um clássico')