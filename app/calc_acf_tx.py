import sqlite3
import fuzzy
from calc_metas import calc_metas, calc_temposistema
from soma_sensores import soma_sensores
from agregar_sensores_aut import agregar_sensores_aut

def autonomia_s(id):
    # S1 -- contagem de lavagem de maos
    conn = sqlite3.connect('app.db')
    cur = conn.cursor()
    cur.execute('SELECT meta_1 FROM user WHERE id='+str(id))
    valor_s1 = cur.fetchone()[0]
    s1 = (fuzzy.calcfuzzy(valor_s1, 1, 6))
    conn.close()
    maior_fuzzy_s1 = max(s1)
    for i in range(len(s1)):
        if s1[i] == maior_fuzzy_s1:
            s1[i] = 1
        else:
            s1[i] = 0

    # S2 -- tempo no sistema
    conn = sqlite3.connect('app.db')
    cur = conn.cursor()
    cur.execute('SELECT meta_3 FROM user WHERE id='+str(id))
    valor_s2 = cur.fetchone()[0]
    s2 = (fuzzy.calcfuzzy(valor_s2, 1, 4))
    conn.close()
    maior_fuzzy_s2 = max(s2)
    for i in range(len(s2)):
        if s2[i] == maior_fuzzy_s2:
            s2[i] = 1
        else:
            s2[i] = 0

    # S3 -- clicou nas noticias
    conn = sqlite3.connect('app.db')
    cur = conn.cursor()
    cur.execute('SELECT readnews FROM user WHERE id='+str(id))
    valor_s3 = cur.fetchone()[0]
    if valor_s3 == 1:
        valor_s3_ = 6
    else:
        valor_s3_ = 1
    s3 = (fuzzy.calcfuzzy(valor_s3_, 1, 6))
    conn.close()
    maior_fuzzy_s3 = max(s3)
    for i in range(len(s3)):
        if s3[i] == maior_fuzzy_s3:
            s3[i] = 1
        else:
            s3[i] = 0

    autonomia_s = (agregar_sensores_aut(s1, s2, s3))
    return autonomia_s
#qualquer um desses
   # return (soma_sensores(s1, s2, s3))
 #   return (agregar_sensores_aut(s1, s2, s3))



def competencia_s(id):
    # S4 -- prencher metas
    conn = sqlite3.connect('app.db')
    cur = conn.cursor()
    cur.execute('SELECT meta_1, meta_2, meta_3 FROM user WHERE id='+str(id)) #mudar id
    valor_s4 = cur.fetchall()
    for linha in valor_s4:
         soma = sum(linha)
    s4 = (fuzzy.calcfuzzy(soma, 1, 6))
    conn.close()
    maior_fuzzy_s4 = max(s4)
    for i in range(len(s4)):
        if s4[i] == maior_fuzzy_s4:
            s4[i] = 1
        else:
            s4[i] = 0

    # S5 -- numero de metas batidas(trofeus)
    conn = sqlite3.connect('app.db')
    cur = conn.cursor()
    cur.execute('SELECT meta_1, meta_2, meta_3 FROM user WHERE id='+str(id)) #mudar id
    valor_s5 = cur.fetchall()
    for linha in valor_s5:
         soma = (sum(linha)/3)  #rever esse calculo pq da baixo
    s5 = (fuzzy.calcfuzzy(soma, 1, 6))
    conn.close()
    maior_fuzzy_s5 = max(s5)
    for i in range(len(s5)):
        if s5[i] == maior_fuzzy_s5:
            s5[i] = 1
        else:
            s5[i] = 0
   

    # S6 resposta a gatilhos
    conn = sqlite3.connect('app.db')
# Cria um objeto Cursor
    cur = conn.cursor()
    # Executa uma consulta SELECT
    cur.execute('SELECT meta_2 FROM user WHERE id='+str(id)) #mudar id
    valor_s6 = cur.fetchone()[0]
    if valor_s6 == 1:
        valor_s6_ = 6
    else:
        valor_s6_ = 1
    s6 = (fuzzy.calcfuzzy(valor_s6_, 1, 6))
    conn.close()
    maior_fuzzy_s6 = max(s6)
    for i in range(len(s6)):
        if s6[i] == maior_fuzzy_s6:
            s6[i] = 1
        else:
            s6[i] = 0
            
    competencia_s = (agregar_sensores_aut(s4, s5, s6))
    return competencia_s
  #  return (agregar_sensores_aut(s4, s5, s6))
##################################################################

def afinidade_s(id):
    # S7 -- prencher data de nascimento
    conn = sqlite3.connect('app.db')
    cur = conn.cursor()
    cur.execute('SELECT dob FROM user WHERE id='+str(id)) #mudar id
    valor_s7 = cur.fetchone()[0]
    if valor_s7:
        valor_s7_ = 6
    else:
        valor_s7_ = 1
 
    s7 = (fuzzy.calcfuzzy(valor_s7_, 1, 6))
    conn.close()
    maior_fuzzy_s7 = max(s7)
    for i in range(len(s7)):
        if s7[i] == maior_fuzzy_s7:
            s7[i] = 1
        else:
            s7[i] = 0
    
     # S8 -- prencher nacionalidade
    conn = sqlite3.connect('app.db')
    cur = conn.cursor()
    cur.execute('SELECT nationality FROM user WHERE id='+str(id)) #mudar id
    valor_s8 = cur.fetchone()[0]
    if valor_s8:
        valor_s8_ = 6
    else:
        valor_s8_ = 1
    s8 = (fuzzy.calcfuzzy(valor_s8_, 1, 6))
    conn.close()
    maior_fuzzy_s8 = max(s8)
    for i in range(len(s8)):
        if s8[i] == maior_fuzzy_s8:
            s8[i] = 1
        else:
            s8[i] = 0
   

    # S9 numero de login
    conn = sqlite3.connect('app.db')
# Cria um objeto Cursor
    cur = conn.cursor()
    # Executa uma consulta SELECT
    cur.execute('SELECT count_login FROM user WHERE id='+str(id)) #mudar id
    valor_s9 = cur.fetchone()[0]
    if valor_s9 == 1:
        valor_s9_ = 1
    elif valor_s9 == 2:
        valor_s9_ = 2
    elif valor_s9 == 3:
        valor_s9_ = 3
    elif valor_s9 == 4:
        valor_s9_ = 4
    elif valor_s9 == 5:
        valor_s9_ = 5
    else:
        valor_s9_ = 6
    s9 = (fuzzy.calcfuzzy(valor_s9_, 1, 6))
    conn.close()
    maior_fuzzy_s9 = max(s9)
    for i in range(len(s9)):
        if s9[i] == maior_fuzzy_s9:
            s9[i] = 1
        else:
            s9[i] = 0
    
    afinidade_s = (agregar_sensores_aut(s7, s8, s9))
    return afinidade_s
            
#autonomia_saida = autonomia()
#competencia_saida = competencia()
#afinidade_saida = afinidade()




#print(autonomia_saida)
#print('------------')
#print(competencia_saida)
#print('------------')
#print(afinidade_saida)