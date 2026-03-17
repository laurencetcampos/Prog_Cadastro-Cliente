import mysql.connector

config = {
    'user': 'root',
    'password': '123456',
    'host': 'localhost',
    'database': 'cadastro_clientes'
}
def cnx():
    try:
        conexao = mysql.connector.connect(**config)
        print("Conectado com sucesso!")
        return conexao

    except mysql.connector.Error as err:
        print("Erro ao conectar com MySQL:", err)
        return None