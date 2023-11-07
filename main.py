import mysql.connector


conexao = mysql.connector.connect(
    host ='localhost',
    user='root',
    password='151029',
    database='bdjuan',
)

cursor = conexao.cursor()

# CREATE
def create():
    nome_produto = 'Café'
    valor = 3
    comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}","{valor}")'
    cursor.execute(comando)
    conexao.commit()
# READ
def read():
    comando = 'SELECT * FROM vendas'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    return resultado

# UPDATE
def update():
    valor = 2
    idVendas = 7
    comando = f'UPDATE vendas SET valor = "{valor}" WHERE idVendas = "{idVendas}"'
    cursor.execute(comando)
    conexao.commit()

def delete():
    idVendas = 2
    comando = f'DELETE FROM vendas WHERE "{idVendas}"'
    cursor.execute(comando)
    conexao.commit()


cursor.close()
conexao.close()



