# Importa a função de conexão com o banco de dados
from DB_connection import cnx
import mysql.connector  # Biblioteca para interagir com MySQL

# Função para cadastrar um novo cliente no banco de dados
def post_cliente(nome, whatsapp, endereco, cidade, status):
    # Estabelece conexão com o banco de dados
    conexao = cnx()

    # Verifica se a conexão foi bem-sucedida
    if conexao is None:
        return  # Sai da função se não conseguir conectar

    # Cria um cursor para executar comandos SQL
    cursor = conexao.cursor()

    try:
        # Executa o comando INSERT para adicionar o cliente na tabela
        cursor.execute(
            """INSERT INTO clientes (nome_cliente, whatsapp, endereco, cidade, promocao_status)
            VALUES (%s, %s, %s, %s, %s)""",
            (nome, whatsapp, endereco, cidade, status)  # Parâmetros para evitar SQL injection
        )
        # Confirma a transação no banco
        conexao.commit()
        print("Cliente inserido com sucesso!")
    except mysql.connector.Error as err:
        # Em caso de erro, desfaz a transação
        conexao.rollback()
        print("Erro ao cadastrar cliente:", err)
    finally:
        # Fecha o cursor e a conexão, independentemente do resultado
        cursor.close()
        conexao.close()

    