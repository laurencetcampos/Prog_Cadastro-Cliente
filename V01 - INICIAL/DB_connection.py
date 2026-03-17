import mysql.connector

config = {
    'user': '',
    'password': '',
    'host': '',
    'database': ''
}
def cnx():
    try:
        conexao = mysql.connector.connect(**config)
        print("Conectado com sucesso!")
        return conexao

    except mysql.connector.Error as err:
        print("Erro ao conectar com MySQL:", err)
        return None