import sqlite3

connection  = sqlite3.connect('banco.db')
cursor = connection.cursor()

cria_tabela = "CREATE TABLE IN NOT EXISTS hoteis (hotel_id text PRIMARY KEY, \
        nome text, estrelas real, diaria real, cidade text)"

cursor.execute(cria_tabela)
connection.close()