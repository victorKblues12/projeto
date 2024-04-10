import sqlite3

# 1 - Criando 
conexao = sqlite3.connect('diretores.db')
cursor = conexao.cursor()

# 2 - Exclusão
id = 4
cursor.execute(
    ''' DELETE FROM diretoresCinema
    WHERE id = ?
    ''',
    (id,)
)

conexao.commit()