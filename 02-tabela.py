import sqlite3

# 1 - Conectando no Banco de Dados
conexao = sqlite3.connect('diretores.db')

cursor = conexao.cursor()

# 2 - Criação da tabela (query)
cursor.execute(
'''
    CREATE TABLE diretoresCinema(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    filmes TEXT  NOT NULL,
    idade INTERGER NOT NULL,
    estilo TEXT NOT NULL,
    notaMedia REAL NOT NULL
    );
'''
)

# 3 - Fechando conexão
conexao.close()
print('Claro que deu certo!')