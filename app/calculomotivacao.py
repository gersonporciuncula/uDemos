
import soma_vetores
import mult_mat_vet
import mult_vet_const
import soma_elem_do_vet
import transposta
import calculo_pesos
import mult_mat_const

 
def calculomotivacao(MotivationS, autonomia, competencia, afinidade):

   nAU = 6
   nComp =6
   nafin =6 
   nM = 6 # nro neuronios
   sigma = 0.5
   Mu = 4
   Ms = [1,2,3,4,5,6]
   AUsigma = 1.5
   AUmu = 4

   WCANN = calculo_pesos.calculo_pesos(sigma, Ms)
   Wau_m = calculo_pesos.calculo_pesos(AUsigma, Ms)
   Wcomp_m = calculo_pesos.calculo_pesos(AUsigma, Ms)
   Wrel_m = calculo_pesos.calculo_pesos(AUsigma, Ms)
   wneed = [0.5, 0.5, 0.5, 0.2, 0.1, 0.4]
   MotivationC = [1,0,0,0,0,0]

   mult_mat_autonomia = []
   mult_mat_competencia= []
   mult_mat_afinidade = []
   mult_mat_MotivationS= []
   mult_mat_MotivationC = []
   motS = []
   aut = []
   comp =[]
   afin =[]
   mprev =[]
   Mcontex =[]
  #somafatmot =[]
   motivacao= []


 
   mult_mat_autonomia = mult_mat_const.mult_mat_const(Wau_m,wneed[0])
   mult_mat_competencia= mult_mat_const.mult_mat_const(Wcomp_m,wneed[1])
   mult_mat_afinidade = mult_mat_const.mult_mat_const(Wrel_m,wneed[2])
   
   aut = mult_mat_vet.mult_mat_vet(mult_mat_autonomia,autonomia)
   comp = mult_mat_vet.mult_mat_vet(mult_mat_competencia,competencia)
   afin = mult_mat_vet.mult_mat_vet(mult_mat_afinidade,afinidade)
# ate aqui ok
   mprev = mult_vet_const.mult_vet_const(MotivationS,wneed[3]) 
   Mcontex = mult_vet_const.mult_vet_const(MotivationC,wneed[4])
   soma_elem_vet = soma_elem_do_vet.soma_elem_do_vet(wneed)
   div_soma_elem = 1/soma_elem_vet

  



   soma_vets = soma_vetores.soma_vetores(aut,comp,afin,mprev,Mcontex)
   motivacao = mult_vet_const.mult_vet_const(soma_vets,div_soma_elem)
   i = 0
   motS = [0] * nAU 
   #for i in range(nAU):
   while i < nAU:
      motS[i] = 0
      i += 1
   #print(motS)

   val_estado_mais_provavel = max(motivacao)
   #est_estado_mais_provavel = motivacao.index(val_estado_mais_provavel) + 1
   est_estado_mais_provavel = motivacao.index(val_estado_mais_provavel)

   motS[est_estado_mais_provavel] = 1

   return motS



#autonomia = [0, 1, 0, 1, 1, 0]
#competencia= [0, 1, 0, 0, 1, 0]
#afinidade = [1, 0, 0, 0, 1, 0]
#MotivationS = [0, 0, 0, 1, 0, 0]

#x = calculomotivacao (MotivationS, autonomia, competencia, afinidade)

#print(x)