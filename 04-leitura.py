import sqlite3

conexao = sqlite3.connect('diretores.db')
cursor = conexao.cursor()

# 2 - leitura de dados
dados = cursor.execute(
    '''SELECT * FROM diretoresCinema'''
)
print(dados.fetchall())
