import schedule
import time
import sqlite3
from bpnss import  autonomia, competencia, afinidade #faz o primeiro calculo
from sims import calc_motivacao_inicial
from calculomotivacao import calculomotivacao
from calc_acf_tx import autonomia_s, competencia_s, afinidade_s #faz o restante dos calculos usando os sensores
import json

def MotivacaoInicial():
    conn = sqlite3.connect('app.db')
    cur = conn.cursor()
    cur.execute('SELECT id FROM user WHERE questionario = 1 and bpnss = 1')
    usuarios = cur.fetchall()
    for id_user in usuarios:
        motivacaoS = calc_motivacao_inicial(id_user[0])    #ok
  
        mot = calculomotivacao(motivacaoS, autonomia(id_user[0]), competencia(id_user[0]), afinidade(id_user[0])) #ok
        motivacao_json = json.dumps(mot)
        cur.execute('UPDATE user SET motivacao=? WHERE id=?',(motivacao_json,id_user[0]))
        conn.commit()
        cur.execute('UPDATE user SET questionario = 0, bpnss = 0 WHERE id=?',(id_user[0],))
        conn.commit()
      #  print(mot)
    conn.close()
    
def MotivacaoAtual():
    conn = sqlite3.connect('app.db')
    cur = conn.cursor()
    cur.execute('SELECT id, motivacao FROM user WHERE questionario = 0 and bpnss = 0')
    usuarios = cur.fetchall()
    for id_user in usuarios:
        motivacaoS = eval(id_user[1])
        mot = calculomotivacao(motivacaoS, autonomia_s(id_user[0]), competencia_s(id_user[0]), afinidade_s(id_user[0]))
        motivacao_json = json.dumps(mot)
        cur.execute('INSERT INTO motiv_usuario (motivacao, id_user ) VALUES (?,?)',(motivacao_json,id_user[0]))
        conn.commit()
    conn.close()


a = MotivacaoInicial()
print(a)

b = MotivacaoAtual()
print(b)
schedule.every(1).minutes.do(MotivacaoInicial)
schedule.every(2).minutes.do(MotivacaoAtual)

while True:
    schedule.run_pending()
    time.sleep(1)
