import numpy as np
def soma_vetores(aut, comp, afin, mprev, mcontext):

    resultado = []
   
    nlinhasVet = len(aut)
  #  print(nlinhasVet)
    if(nlinhasVet == len(comp) == len(afin) == len(mprev) == len(mcontext)):
        
        for i in range(nlinhasVet):
            linha = []
            
            linha.append(0.0)
            resultado.append(linha)
        #print(resultado)
       # print('----')
        for i in range(nlinhasVet):
         #   print(i)
          #  print(resultado[i])
            resultado[i] = np.sum(aut[i] + comp[i] + afin[i] + mprev[i] + mcontext[i])
           
           # print(resultado[i])

        return resultado

    else:
        return "O número de colunas e de linhas são de tamanhos diferentes. (func soma_vetores)"

### OK ###
#print(soma_vetores([1,1,1,1,1,0], [1,1,1,1,1,1], [1,1,1,1,1,1], [0.03334,0.03334,0.03334,0.03334,0.03334,0.03334],[0,0,0,0,0,0.1]))

