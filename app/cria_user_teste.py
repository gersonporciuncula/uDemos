
import sqlite3

# Conecta ao banco de dados
conn = sqlite3.connect('app.db')

# Cria um objeto Cursor
cur = conn.cursor()


# Executa uma consulta SELECT
cur.execute('SELECT * FROM user WHERE id=1 ')

# Recupera todos os resultados da consulta
cursor = cur.fetchall()

# Itera pelos resultados e imprime cada linha
for linha in cursor:
    print(linha)
   
   # sum = sum + linha
# Fecha a conexão
conn.close()