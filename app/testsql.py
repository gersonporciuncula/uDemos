''''
import sqlite3
import fuzzy

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


#####################################
import calc_metas
a = calc_metas.calc_temposistema(1)
print(a)

'''

import sqlite3

# abrir conexão com o banco de dados
conn = sqlite3.connect('app.db')


mot_int = ['Você está fazendo um ótimo trabalho se prevenindo.',
               'Muito Bem! você sempre lavou as mãos! Não esqueça de lavá-las agora.',
               'Muito bem! Você está contribuindo para o combate ao Covid, se prevenindo dessa forma.',
               'Você lavou as mãos 4 vezes no dia de hoje. Parabéns!',
               'Você se esforçou e ajudou a reduzir a contaminação, não participando de aglomerações.',
               'Você está contribuindo para a redução de casos no país.']
    
    # Motivao extrinseca

    # Regulacao integrada
mot_ext_int = ['Higienize as mãos e continue reduzindo a chance de contrair Covid19.',
               'Lave as suas mãos e continue fazendo um bom trabalho.',
               'Continue ajudando aos outros, se higienizando e mantendo o distanciamento.',
               'Mantenha sua máscara e lave suas mãos.',
               'Use a máscara e continue evitando a transmissão do vírus.',
               'Mantenha o uso de máscara e a higienização correta das mãos e contribua para a redução de casos na sua região.']
    
    # Regulacao Identificada
mot_ext_ide = ['Ao lavar as mãos e usar máscara você evita o contágio e propagação do vírus.',
                   'Faça seu ambiente mais saudável ao prevenir-se e a ajudar os outros.',
                   'Previna-se e reduza a chance de contágio.',
                   'Você está sem máscara. Use-a e ajude a conter o avanço da doença.',
                   'Ao prevenir-se  você está contribuindo para a redução de casos na sua região.',
                   'Você lavou as mãos oito vezes este dia! Não esqueça de lavá-las novamente.']
    # Regulacao Introjetada
mot_ext_intr = ['Você deve usar a máscara ao entrar em um ambiente com mais pessoas.',
                    '70% das pessoas deste local usam máscara. Use você também.',
                    'Fique tranquilo porque estou verificando seu uso de máscara e a frequência que higieniza as mãos. Aliás, lave-as agora.',
                    'Você deve proporcionar um ambiente mais seguro, previna-se.',
                    'Você está aumentando a chance de contrair o vírus ao não utilizar mascara em lugares públicos.',
                    'O Brasil está com aumento de casos, previna-se.']
    # Regulacao Externa
mot_ext_ext = ['Você tem que usar máscara e higienizar as mãos para reduzir a chance de contágio.',
                   'Você tem que usar máscara ao sair para rua.',
                   'Você não está lavando as mãos com frequência.',
                   'Olá usuário, eu sou o uDemos! O cara que irá lembrá-lo que você esqueceu de lavar as mãos e utilizar máscara. Previna-se.',
                   'Você tem que contribuir com a redução da disseminação do vírus, para isso previna-se.',
                   'O número de casos na sua região aumentou e você pode ser um dos culpados. Por isso você deve higienizar as suas mãos com mais frequência e sempre utilizar máscara.']

falta_motivacao = ['Use mais máscara e contribua com a redução de casos de COVID-19.',
                       'Vamos reduzir a contaminação?! Clique em compartilhar as dicas, para ajudar outras pessoas a se prevenir.',
                       'Minha experiência em se prevenir garante que não vai se prejudicar usar máscara durante todo o tempo e higienizar as mãos frequentemente. Confie em mim e lave-as mãos agora mesmo.',
                       'Se você não lavar as mãos com frequência, a chance de contágio aumenta muito. Então lave-as.',
                       'Você reduzirá muito ao utilizar máscara durante todo o tempo.',
                       'Sua região aumentou os casos novamente, por isso previna-se, para que não sofre com superlotação em hospitais.']
    
    


# inserir as mensagens na tabela
for mensagem in mot_int:
    conn.execute("INSERT INTO mot_int (msg) VALUES (?)", (mensagem,))
    
# confirmar as alterações
conn.commit()

for mensagem in mot_ext_int:
    conn.execute("INSERT INTO mot_ext_int (msg) VALUES (?)", (mensagem,))

# confirmar as alterações
conn.commit()   

for mensagem in mot_ext_ide:
    conn.execute("INSERT INTO mot_ext_ide (msg) VALUES (?)", (mensagem,))

# confirmar as alterações
conn.commit() 

for mensagem in mot_ext_intr:
    conn.execute("INSERT INTO mot_ext_intr (msg) VALUES (?)", (mensagem,))

# confirmar as alterações
conn.commit() 

for mensagem in mot_ext_ext:
    conn.execute("INSERT INTO mot_ext_ext (msg) VALUES (?)", (mensagem,))

# confirmar as alterações
conn.commit() 

for mensagem in falta_motivacao:
    conn.execute("INSERT INTO falta_motivacao (msg) VALUES (?)", (mensagem,))

# confirmar as alterações
conn.commit() 

# fechar conexão com o banco de dados
conn.close()


#pbkdf2:sha256:260000$BRPcfwEnfU2x0bin$20de81d3bec4ebe1b005604cfb230b08bc56dc7d095606503551ef69d7e64ba0	