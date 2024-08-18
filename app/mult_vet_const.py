def mult_vet_const(vet, valor):

    resultado = []
 
    nlinhasVet = len(vet)

    for i in range(nlinhasVet):
        linha = []
        linha.append(0)
        resultado.append(linha)
    
    for i in range(nlinhasVet):
            resultado[i] = vet[i]*valor
    
    return resultado

### OK ###