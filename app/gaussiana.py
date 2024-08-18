import math

def generateGaussian(sig, mi, vet):

    resultado = []
    ncolunasVet = len(vet)
    nlinhasVet = len(vet)

    a = (1/(sig*math.sqrt(2*math.pi)))
    k = 0

    for i in range(nlinhasVet):
        linha = []
        for j in range(ncolunasVet):
            linha.append(0.0)
        resultado.append(linha)
    
 
    for j in range(ncolunasVet):
            k = vet[j] - mi
            y = math.pow(k, 2)
            yy = math.pow(sig, 2)
            resultado[j] = a*math.exp(-y/(2*yy))

    return resultado

### OK ###
	