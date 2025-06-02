# Nesse exercício coletaremos dados de uma estudante, armazenaremos em um dicionário e imprimiremos na tela esse dados em um formato amigável.

# 1. Solicite a estudante os seguintes dados: nome, ano que conheceu o LinkedIn, ano atual e os cursos realizados no LinkedIn Learning separados por virgula em ordem cronológica

estudante={}
estudante['nome'] = input('Qual o seu nome? ')
estudante['ano_conheceu_linkedin'] = int(input('Em que ano conheceu o linkedin?'))
estudante['ano_atual'] = int(input('Qual o ano atual?'))
cursos = input('Quais os cursos que ja realizou no linkedin learning? (Separe-os por virgula) ')

# 2. Armazene esses dados em um dicionário
# 3. Imprima na tela uma string com as informações de nome, ano_conheceu_linkedin, total de anos transcurridos, total de cursos realizados e (apenas) o primeiro e último curso.

estudante['cursos'] = cursos.split(', ')

print(f"Oi {estudante['nome']}, desde {estudante['ano_conheceu_linkedin']} você conhece o LinkedIn. Nesses {estudante['ano_atual'] - estudante['ano_conheceu_linkedin']} anos, você realizou {len(estudante['cursos'])} cursos, sendo o primeiro curso '{estudante['cursos'][0]}' e último '{estudante['cursos'][-1]}'.")