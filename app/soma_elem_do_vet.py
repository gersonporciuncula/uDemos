def soma_elem_do_vet(vet):
    
    resultado = 0
   # ncolunasVet = len(vet[0])
    nlinhasVet = len(vet)
    
    for i in range(nlinhasVet):
            resultado += vet[i]
    
    return resultado

### OK ###