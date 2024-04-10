import sqlite3

conexao = sqlite3.connect('diretores.db')

cursor = conexao.cursor()

cursor.execute(
'''
  INSERT INTO diretoresCinema(nome, filmes, idade, estilo, notaMedia)
  VALUES("Quentin Tarantino", "Pulp Fiction, Bastardos Inglórios, Django Livre, Reservoir Dogs, Um Drink no Inferno", 61, "Violência, Sangue, Frenético", 10.00)
'''
)

# Fechando conexão
conexao.commit()
conexao.close()
print('Claro que deu certo!')