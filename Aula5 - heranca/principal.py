from funcionario import Funcionario, Engenheiro, Supervisor

f1 = Funcionario('Joana', 3000)
engenheiro1 = Engenheiro('Koala', 3000)
supervisor1 = Supervisor('Carlos', 4500)

f1.informacoes()

engenheiro1.bonusEngenheiro()
engenheiro1.informacoes()
supervisor1.relatorio()