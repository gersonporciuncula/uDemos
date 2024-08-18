import sqlite3
import fuzzy
from calculomotivacao import calculomotivacao

def autonomia(id):
    conn = sqlite3.connect('app.db')
    cur = conn.cursor()
    cur.execute('SELECT bpnss1, 8-bpnss4, bpnss8, 8-bpnss11, bpnss14, bpnss17, 8-bpnss20 FROM user WHERE id='+str(id))
    autonomia = cur.fetchall()
    for linha in autonomia:
        soma = (sum(linha)/7)
    conn.close()
    fuzzy_aut = (fuzzy.calcfuzzy(soma, 1, 6))
    maior_fuzzy_aut = max(fuzzy_aut)        
    for i in range(len(fuzzy_aut)):
        if fuzzy_aut[i] == maior_fuzzy_aut:
            fuzzy_aut[i] = 1
        else:
            fuzzy_aut[i] = 0
    return fuzzy_aut

def competencia(id):
    conn = sqlite3.connect('app.db')
    cur = conn.cursor()
    cur.execute('SELECT 8-bpnss3, bpnss5, bpnss10, bpnss13, 8-bpnss15, 8-bpnss19 FROM user WHERE id='+str(id))
    competencia = cur.fetchall()
    for linha in competencia:
        soma = (sum(linha)/7)
    conn.close()
    fuzzy_comp = (fuzzy.calcfuzzy(soma, 1, 6))
    maior_fuzzy_comp = max(fuzzy_comp)        
    for i in range(len(fuzzy_comp)):
        if fuzzy_comp[i] == maior_fuzzy_comp:
            fuzzy_comp[i] = 1
        else:
            fuzzy_comp[i] = 0
    return fuzzy_comp


def afinidade(id):
    conn = sqlite3.connect('app.db')
    cur = conn.cursor()
    cur.execute('SELECT bpnss2, bpnss6, 8-bpnss7, bpnss9, bpnss12, 8-bpnss16, 8-bpnss18, bpnss21 FROM user WHERE id='+str(id))
    afinidade = cur.fetchall()
    for linha in afinidade:
        soma = (sum(linha)/7)
    conn.close()
    fuzzy_afin = (fuzzy.calcfuzzy(soma, 1, 6))
    maior_fuzzy_afin = max(fuzzy_afin)        
    for i in range(len(fuzzy_afin)):
        if fuzzy_afin[i] == maior_fuzzy_afin:
            fuzzy_afin[i] = 1
        else:
            fuzzy_afin[i] = 0
    return fuzzy_afin

#print(calculomotivacao(bnpss(2), autonomia(2), competencia(2), afinidade(2)))