import sqlite3
from datetime import datetime

def calc_metas(id):
    # Conecta ao banco de dados
    conn = sqlite3.connect('app.db')
# Cria um objeto Cursor
    cur = conn.cursor()
    # Executa uma consulta SELECT
    cur.execute('SELECT meta_1, meta_2, meta_3 FROM user WHERE id='+str(id))
    # Recupera todos os resultados da consulta
    metas = cur.fetchall()
    # Itera pelos resultados e imprime cada linha
    for linha in metas:
        soma = sum(linha)
    # Fecha a conexão
    conn.close()
    if soma <= 3:
        return 0
    elif soma <= 7:
        return 1
    else:
        return 2
    
  
def calc_temposistema(id):
    conn = sqlite3.connect('app.db')
# Cria um objeto Cursor
    cur = conn.cursor()
    # Executa uma consulta SELECT
    cur = cur.execute('SELECT last_seen, last_logoff FROM user WHERE id=id ')
     # Recupera todos os resultados da consulta
    data = cur.fetchall()
    #login_hora = datetime.strptime(data[0][0], '%d/%m/%Y %H:%M').strftime('%H:%M')
    #logout_hora = datetime.strptime(data[0][1], '%d/%m/%Y %H:%M').strftime('%H:%M')
    login_hora = datetime.strptime(data[0][0], '%d/%m/%Y %H:%M')
    logout_hora = datetime.strptime(data[0][1], '%d/%m/%Y %H:%M')
   # print(login_hora)
   # print(logout_hora)
    conn.close()
    time_in_system = logout_hora - login_hora
    return time_in_system

    
    
#a = calc_metas(1)
#print(a)
  #  return soma

