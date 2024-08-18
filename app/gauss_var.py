import math

def gauss_var(sig, mi, valor):

   # a = (1/(sig*math.sqrt(2*math.pi)))
    a = 1
    k = valor - mi
    y = math.pow(k, 2)
    yy = math.pow(sig, 2)
    resultado = a*math.exp(-y/(2*yy))

    return resultado

### OK ###

#print(gauss_var(1.5,1,2))