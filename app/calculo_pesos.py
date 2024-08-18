import gaussiana

def calculo_pesos(sig, x):

    gauss = []
    somacol = []
    resultado = []

    ncolunasVet = len(x) #pega colunas

    for i in range(ncolunasVet):
        linha = []
        for j in range(ncolunasVet):
            linha.append(None)
        gauss.append(linha)

    for i in range(ncolunasVet):
        linha = []
        for j in range(ncolunasVet):
            linha.append(None)
        resultado.append(linha)

   # mu = mu[0]

    for i in range(ncolunasVet):
        gauss[i] = gaussiana.generateGaussian(sig, i+1, x)

    for i in range(ncolunasVet):
        linha = []
        for j in range(ncolunasVet):
            linha.append(0.0)
        somacol.append(linha)
    
    for i in range(ncolunasVet):
        somacol[i] = 0

    for i in range(ncolunasVet):
        for j in range(ncolunasVet):
            somacol[j] += gauss[i][j]


    for i in range(ncolunasVet):
        for j in range(ncolunasVet):
            resultado[i][j] = gauss[j][i] / somacol[j]

    return resultado

### OK ###




 