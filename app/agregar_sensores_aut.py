def agregar_sensores_aut(vet1, vet2, vet3):

    resultado = []
    need = []

    ncolunasVet = len(vet1)
 

    if(ncolunasVet == len(vet2) == len(vet3)):

        for i in range(ncolunasVet):
            linha = []
            linha.append(0.0)
            resultado.append(linha)

        for i in range(ncolunasVet):
            resultado[i] = max(vet1[i], vet2[i], vet3[i])
        
        #fuzzysaida = resultado[0].index(max(resultado[0]))
        fuzzysaida =   max(resultado)

        for i in range(ncolunasVet):
    # print(fuzzy[i])
            if resultado[i] == fuzzysaida:
                resultado[i] = 1
            else:
                resultado[i] = 0

    

        return resultado

    else:
        return "O número de colunas e de linhas são de tamanhos diferentes. (func agregar_sensores_aut)"

### OK ###