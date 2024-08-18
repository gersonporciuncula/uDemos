import sqlite3
import fuzzy

def calc_motivacao_inicial(id):

    def motivacaointrinseca(id):
        # Conecta ao banco de dados
        conn = sqlite3.connect('app.db')
    # Cria um objeto Cursor
        cur = conn.cursor()
        # Executa uma consulta SELECT
        cur.execute('SELECT sims1, sims5, sims9, sims13 FROM user WHERE id='+str(id))
        # Recupera todos os resultados da consulta
        mot_intrinseca = cur.fetchall()
        # Itera pelos resultados e imprime cada linha
        for linha in mot_intrinseca:
            #print(linha)
            soma = (sum(linha)/4)
        # Fecha a conexão
        conn.close()
        return soma
        
    


    def regulamentoidentificada(id):
        # Conecta ao banco de dados
        conn = sqlite3.connect('app.db')
    # Cria um objeto Cursor
        cur = conn.cursor()
        # Executa uma consulta SELECT
        cur.execute('SELECT sims2, sims6, sims10, sims14 FROM user WHERE id='+str(id))
        # Recupera todos os resultados da consulta
        reg_identificada = cur.fetchall()
        # Itera pelos resultados e imprime cada linha
        for linha in reg_identificada:
            soma = (sum(linha)/4)
        # Fecha a conexão
        conn.close()
        return soma



    def regulacaoexterna(id):
        # Conecta ao banco de dados
        conn = sqlite3.connect('app.db')
    # Cria um objeto Cursor
        cur = conn.cursor()
        # Executa uma consulta SELECT
        cur.execute('SELECT sims3, sims7, sims11, sims15 FROM user WHERE id='+str(id))
        # Recupera todos os resultados da consulta
        reg_externa = cur.fetchall()
        # Itera pelos resultados e imprime cada linha
        for linha in reg_externa:
            soma = (sum(linha)/4)
        # Fecha a conexão
        conn.close()
        return soma

    def faltamotivacao(id):
        # Conecta ao banco de dados
        conn = sqlite3.connect('app.db')
    # Cria um objeto Cursor
        cur = conn.cursor()
        # Executa uma consulta SELECT
        cur.execute('SELECT sims4, sims8, sims12, sims16 FROM user WHERE id='+str(id))
        # Recupera todos os resultados da consulta
        fal_motivacao = cur.fetchall()
        # Itera pelos resultados e imprime cada linha
        for linha in fal_motivacao:
            soma = (sum(linha)/4)
        # Fecha a conexão
        conn.close()   
        return soma

   # print(motivacaointrinseca())
    #print(regulamentoidentificada())
    #print(regulacaoexterna())
    #print(faltamotivacao())

    calculo_final = (2 * motivacaointrinseca(id)) + (1 * regulamentoidentificada(id)) - (1 * regulacaoexterna(id)) - (2 * faltamotivacao(id))


    if calculo_final < 0:
        a = (abs(calculo_final))
        calc = (fuzzy.calcfuzzy(a, 1, 36))

        maior_fuzzy = max(calc)
        for i in range(len(calc)):
            if calc[i] == maior_fuzzy:
                calc[i] = 1
            else:
                calc[i] = 0

        return(calc)

    
    


    else:
        a = ((calculo_final * 36)/18)
        calc = (fuzzy.calcfuzzy(a, 1, 36))
        maior_fuzzy = max(calc)
        for i in range(len(calc)):
            if calc[i] == maior_fuzzy:
                calc[i] = 1
            else:
                calc[i] = 0

        return(calc)