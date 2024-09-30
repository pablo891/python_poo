from livro import Livro


tituloLivro = input('Informe o título do livro: ')
autorLivro = input('Informe o autor do livro: ')
anoPublicacao = int(input('Informe o ano de publicação: '))

livro1 = Livro(tituloLivro, autorLivro, anoPublicacao)
livro1.exibirInformacoes()


livro2 = Livro(tituloLivro, autorLivro, anoPublicacao)
livro2.exibirInformacoes()
livro2.vericarIdadeLivro()