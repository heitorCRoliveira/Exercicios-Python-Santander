# Notas do estudantes
notas = {"1º Trimestre": 8.5, "2º Trimestre": 9.5, "3º trimestre": 7}


# Calculando a soma
soma = 0
for nota in notas.values():
    soma += nota
print(soma)


# Usando a função embutida sum()
somatorio = sum(notas.values())
print(somatorio)


# Usando a função embutida len()
qtd_notas = len(notas)
print(qtd_notas)

# Calculando a média

media = somatorio / qtd_notas
print(round(media, 1))
