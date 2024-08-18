import sqlite3
import fuzzy


conn = sqlite3.connect('app.db')
cur = conn.cursor()
cur.execute('SELECT bpnss1, 8-bpnss4, bpnss8, 8-bpnss11, bpnss14, bpnss17, 8-bpnss20 FROM user WHERE id=1 ')
bpnss = cur.fetchall()
for linha in bpnss:
    soma = (sum(linha)/7)
conn.close()
calc_bpnss = (fuzzy.calcfuzzy(soma, 1, 6))
maior_fuzzy = max(calc_bpnss)
for i in range(len(calc_bpnss)):
    if calc_bpnss[i] == maior_fuzzy:
        calc_bpnss[i] = 1
    else:
        calc_bpnss[i] = 0
print(calc_bpnss)