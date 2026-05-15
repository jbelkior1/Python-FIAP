temperaturas = [
    [28, 31, 34, 33],
    [25, 27, 29, 28],
    [32, 35, 36, 34],
    [24, 26, 25, 27]
]

maior_qtd_criticos = 0
sala_critica = 0


for i in range(len(temperaturas)):
    numero_sala = i + 1
    print(f'Sala {numero_sala}')
    #print(temperaturas[i]) # LINHA = 1 SALA
    qtd_reg_criticos = 0

    for j in range(len(temperaturas[i])):
        #print(temperaturas[i][j]) # UMA TEMPERATURA
        if temperaturas[i][j] >= 33:
            qtd_reg_criticos += 1

    media = sum(temperaturas[i]) / len(temperaturas[i])
    print(f'Média: {media}')
    print(f'Registros críticos nesta sala: {qtd_reg_criticos}')
    print()

    if qtd_reg_criticos > maior_qtd_criticos:
        maior_qtd_criticos = qtd_reg_criticos
        sala_critica = numero_sala

print(f'A sala com maior quantidade de registros críticos é a Sala {sala_critica} com {maior_qtd_criticos} registros.')
