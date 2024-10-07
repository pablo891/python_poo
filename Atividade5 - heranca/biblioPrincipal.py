from biblioteca import Biblioteca, Livro, Revista

bl1 = Biblioteca('O Pequeno Príncipe', ' Antoine de Saint-Exupéry', 1943, 202)
livro1 = Livro('A Metamorfose', 'Franz Kafka', 1915, 361)
revista1 = Revista('Época', '', 1995, 79)

bl1.detalhes()

print('=' * 50)

livro1.detalhes()
livro1.calcularIdadeItem()
livro1.verificarTamanho()

print('=' * 50)

revista1.detalhes()
revista1.calcularIdadeItem()
revista1.verificarEdicao()