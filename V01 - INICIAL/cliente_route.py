from DB_connection import cnx
import mysql.connector

def post_cliente(nome, whatsapp, endereco, cidade, status):
    conexao = cnx()

    if conexao is None:
        return
    
    cursor = conexao.cursor()

    try:
        cursor.execute(
            """INSERT INTO clientes (nome_cliente, whatsapp, endereco, cidade, promocao_status)
            VALUES (%s, %s, %s, %s, %s)""",
            (nome, whatsapp, endereco, cidade, status)  
        )
        conexao.commit()
        print("Cliente inserido com sucesso!")
    except mysql.connector.Error as err:
        conexao.rollback()
        print("Erro ao cadastrar cliente:", err)
    finally:
        cursor.close()
        conexao.close()

    