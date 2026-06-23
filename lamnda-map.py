# ========================================MAP===============================#

# Notas do estudante

notas = [6.0, 7.0, 9.0, 5.5, 8.0]
qualitativo = 0.5

# A função lambda não consegue iterar dentro de uma lista, devido a isso se faz necessário o uso da função map
notas_atualizadas = lambda x: x + qualitativo
# notas_atualizadas(notas)

# Utilizando MAP
notas_atualizadas = map(lambda x: x + qualitativo, notas)
# Convertendo o objeto MAP em list
notas_atualizadas = list(notas_atualizadas)
# Exibindo o resultado
print(notas_atualizadas)
