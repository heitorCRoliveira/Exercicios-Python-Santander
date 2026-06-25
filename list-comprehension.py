# Importando a biblioteca para gerar números aleatórios
from random import randint

# Dados das 3 notas dos 5 alunos
nomes = ["João", "Maria", "José", "Cláudia", "Ana"]
notas = [
    [8.0, 9.0, 10.0],
    [9.0, 7.0, 6.0],
    [3.4, 7.0, 7.0],
    [5.5, 6.6, 8.0],
    [6.0, 10.0, 9.5],
]


# Função para gerar código automático 3 dígitos
def gerar_codigo():
    return str(randint(0, 999))


# Função para calcular a média das notas dos alunos
def media(lista: list = [0]) -> float:
    calculo = sum(lista) / len(lista)

    return calculo


# List Comprehension - Efetua a iteração na lista de listas e insere
medias = [round(media(nota), 1) for nota in notas]

# Verificando informações
print(medias)

# Gerando o código de cada aluno e armazenando na tupla
codigo_estudantes = []

for i in range(len(nomes)):

    codigo_estudantes.append((nomes[i], nomes[i][0] + gerar_codigo()))

# Verificando informações
print(codigo_estudantes)

# Gerando a lista de nomes (extraindo da tupla)
alunos = [nome[0] for nome in codigo_estudantes]
print(alunos)

# Unindo aluno e nota
estudantes = list(zip(alunos, medias))
print(estudantes)


# Gerando lista de pessoas candidatas com bolsa

candidato = [estudante[0] for estudante in estudantes if estudante[1] >= 8.0]

print(candidato)
