# Estrutura  >> lambda <variavel> : expressao

# Comparando uma função de qualitativo no formato de uma função para função anônima
nota = float(input("Digite a nota do estudante: "))


def qualitativo(x):
    return x + 0.5


print(qualitativo(nota))


# Testando a mesma função para uma função lambda
nota = float(input("Digite a nota do estudante: "))

qualitativo = lambda x: x + 0.5

print(qualitativo(nota))

# Recebendo notas e calculando média ponderável

N1 = float(input("Digite a 1ª nota do(a) estudante: "))
N2 = float(input("Digite a 2ª nota do(a) estudante: "))
N3 = float(input("Digite a 3ª nota do(a) estudante: "))

media_ponderavel = lambda x, y, z: (x * 3 + y * 2 + z * 5) / 10
media_estudante = media_ponderavel(N1, N2, N3)
print(f"O estudante obteve a média de {media_estudante}")
