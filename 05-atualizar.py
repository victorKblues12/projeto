import sqlite3

conexao = sqlite3.connect('diretores.db')
cursor = conexao.cursor()

# 2 - Atualizar tabela
id = 1
cursor.execute(
    ''' UPDATE diretoresCinema set filmes= ?
    WHERE id = ?
    ''',
    ("Bastardos Inglórios, Django Livre, Pulp Fiction, ", id)
)

conexao.commit()
