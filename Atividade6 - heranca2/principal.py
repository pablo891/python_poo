from personagem import Personagem, Heroi, Vilao

print('Bem-vindo(a) ao game de Combate !')

while True:
    print('-' * 150)
    print('\n')
    iniciar = int(input('Deseja iniciar o jogo? \n[1] Sim [2] Não\n'))
    if iniciar == 1:

        # Declaração de objetos
        personagem1 = Personagem('Dr. Esperança' , 100, 'Avançado')
        heroi1 = Heroi('Capitão Valor', 100, 'Lendário', 'Frank Charlton (Doutor)')
        vilao1 = Vilao('Sombra Maligna', 100, 'Avançado')

        # Detalhes do Objeto 1
        personagem1.detalhes()
        personagem1.receberDano(80)
        personagem1.verificarVida()
        personagem1.detalhes()

        # Detalhes do Objeto 2
        print('-' * 50)
        print('RODADA DO HERÓI')
        heroi1.detalhes()
        heroi1.receberDano(60)
        heroi1.verificarVida()

        tipoHab = input('Informe o poder: ')
        energiaHab = int(input('Informe o consumo de energia do poder: ')) 
        heroi1.executarHabilidade(tipoHab, energiaHab)

        energiaRecharge = int(input('Informe a quantidade de energia a ser recarregada: '))
        heroi1.recarregarEnergia(energiaRecharge)

        aliado = input('Qual aliado você deseja chamar ?\n')
        descHab = input('Descreva a habilidade do personagem: ')
        heroi1.chamarAliado(aliado, descHab)
        heroi1.detalhes()
        
        # Detalhes do Objeto 3
        print('-' * 50)
        print('RODADA DO VILÃO')

        vilao1.detalhes()
        vilao1.receberDano(40)
    
        tipoGolpe = input('Qual golpes você deseja desferir? ')
        malicia = int(input('Informe o consumo de malícia do golpe: '))
        vilao1.desferirGolpe(tipoGolpe, malicia)

        armadilha = input('Informe a armadilha que deseja fazer: ')
        vilao1.planejarArmadilha(armadilha)
        vilao1.verificarVida()

        vilao1.detalhes()
        if vilao1.vida > 0:
            print('\n')
            cont = int(input('Deseja fugir? [1] Sim [2] Não\n'))
            if cont == 1:
                fuga = input('Qual o modo de fuga? \n')
                vilao1.fugir(fuga)
            elif cont != 1:
                print('Fim do jogo.')
                break
        vilao1.detalhes()
        print('Fim de jogo')

    # Condicionais de finalização
    elif iniciar == 2:
        print('Obrigado por jogar!')
        break

    else:
        print('Opção inválida')
        break