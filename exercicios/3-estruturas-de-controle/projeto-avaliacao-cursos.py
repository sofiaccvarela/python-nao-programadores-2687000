# Nesse desafio você verificará dentro de uma lista se o item estar contido nela, caso verdadeiro deverá imprimir na tela essa informação, além disso deverá solicitar avaliação para o item e armazená-la em um dicionário.
# 1. Crie uma lista com 5 diferentes cursos do LinkedIn Learning

cursos_linkedin = ['Introdução SQL', 'Python: Formação Básica', 'Python para Ciência de Dados: Formação Básica',
                  'Descubra a Linguagem de Programação R', 'Fundamentos de Programação: Algoritmos']

# 2. Crie 3 variáveis do tipo string e associe 1 curso a cada uma delas

curso_git = 'Git e GitHub: Formação Básica'
curso_python = 'Python: Formação Básica'
curso_r = 'Descubra a linguagem de Programação R'

# 3. Crie um dicionário vazio para armazenar a nota do curso

avaliacoes = {}

# 4. Crie uma estrutura condicional para verificar se cada variável está contida na lista

if curso_python in cursos_linkedin:
  print(f'O curso "{curso_python}" está no catalogo. Por favor, avalie o curso.')
  avaliacoes[curso_python]= int(input('Qual é a nota que você dá para o curso (0 a 5)?'))

if curso_git in cursos_linkedin:
  print(f'O curso "{curso_git}" está no catalogo. Por favor, avalie o curso.')
  avaliacoes[curso_git]= int(input('Qual é a nota que você dá para o curso (0 a 5)?'))

if curso_r in cursos_linkedin:
  print(f'O curso "{curso_r}" está no catalogo. Por favor, avalie o curso.')
  avaliacoes[curso_r]= int(input('Qual é a nota que você dá para o curso (0 a 5)?'))
else:
  print("Infelizmente o curso não compoe o nosso catalogo.")
# 5. Se o curso estiver na lista, solicite uma nota para avaliação
# 6. Armazene essa nota no dicionário, sendo a chave o título do curso e o valor a nota

