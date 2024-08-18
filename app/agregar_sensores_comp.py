def agregar_sensores_comp(vet1, vet2, vet3, vet4, vet5):

    resultado = []
    need = []

    ncolunasVet = len(vet1[0])
    nlinhasVet = len(vet1)

    if(ncolunasVet == len(vet2[0]) == len(vet3[0]) == len(vet4[0]) == len(vet5[0])):

        for i in range(nlinhasVet):
            linha = []
            for j in range(ncolunasVet):
                linha.append(0.0)
            resultado.append(linha)

        for i in range(nlinhasVet):
            for j in range(ncolunasVet):
                resultado[i][j] = max(vet1[i][j], vet2[i][j], vet3[i][j], vet4[i][j], vet5[i][j])
        
        fuzzysaida = resultado[0].index(max(resultado[0]))

        for i in range(nlinhasVet):
            linha = []
            for j in range(ncolunasVet):
                linha.append(0.0)
            need.append(linha)

        need[0][fuzzysaida] = 1.0

        return need

    else:
        return "O número de colunas e de linhas são de tamanhos diferentes. (func agregar_sensores_comp)"

### OK ###