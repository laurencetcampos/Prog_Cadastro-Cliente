from DB_connection import cnx
import mysql.connector

# Função POST (Create): Insere um novo registro de cliente na tabela do banco de dados
def post_cliente(nome, whatsapp, endereco, cidade, status):
    conexao = cnx()

    if conexao is None:
        return
    
    cursor = conexao.cursor()

    try:
        # Comando SQL de inserção
        cursor.execute(
            """INSERT INTO clientes (nome_cliente, whatsapp, endereco, cidade, promocao_status)
            VALUES (%s, %s, %s, %s, %s)""",
            (nome, whatsapp, endereco, cidade, status)  
        )
        conexao.commit() # Efetiva a gravação
        print("Cliente inserido com sucesso!")
    except mysql.connector.Error as err:
        conexao.rollback() # Desfaz a operação em caso de erro (ex: WhatsApp duplicado)
        print("Erro ao cadastrar cliente:", err)
    finally:
        # Garante que a conexão seja fechada liberando recursos
        cursor.close()
        conexao.close()

# Função GET All (Read): Retorna uma lista com todos os clientes cadastrados
def get_clientes():
    conexao = cnx()
    if conexao is None: return []
    
    cursor = conexao.cursor(dictionary=True)
    try:
        # Busca generalizada
        cursor.execute("SELECT * FROM clientes")
        clientes = cursor.fetchall()
        return clientes
    except mysql.connector.Error as err:
        print("Erro ao buscar clientes:", err)
        return []
    finally:
        cursor.close()
        conexao.close()

# Função GET By ID (Read Específico): Retorna os dados de apenas um cliente usando a chave primária (ID)
def get_cliente_by_id(id_cliente):
    conexao = cnx()
    if conexao is None: return None
    
    cursor = conexao.cursor(dictionary=True)
    try:
        # Busca filtrada com a cláusula WHERE
        cursor.execute("SELECT * FROM clientes WHERE id_cliente = %s", (id_cliente,))
        cliente = cursor.fetchone()
        return cliente
    except mysql.connector.Error as err:
        print("Erro ao buscar cliente por ID:", err)
        return None
    finally:
        cursor.close()
        conexao.close()

# Função PUT/UPDATE (Update): Modifica as informações de um cliente já existente no banco
def update_cliente(id_cliente, nome, whatsapp, endereco, cidade, status):
    conexao = cnx()
    if conexao is None: return
    
    cursor = conexao.cursor()
    try:
        # Comando SQL de atualização localizando a linha correta pelo WHERE
        cursor.execute(
            """UPDATE clientes SET nome_cliente = %s, whatsapp = %s, endereco = %s, cidade = %s, promocao_status = %s
            WHERE id_cliente = %s""",
            (nome, whatsapp, endereco, cidade, status, id_cliente)
        )
        conexao.commit()
        print("Cliente atualizado com sucesso!")
    except mysql.connector.Error as err:
        conexao.rollback()
        print("Erro ao atualizar cliente:", err)
    finally:
        cursor.close()
        conexao.close()

# Função DELETE (Delete): Apaga definitivamente a linha do cliente no banco de dados
def delete_cliente(id_cliente):
    conexao = cnx()
    if conexao is None: return
    
    cursor = conexao.cursor()
    try:
        cursor.execute("DELETE FROM clientes WHERE id_cliente = %s", (id_cliente,))
        conexao.commit()
        print("Cliente removido com sucesso!")
    except mysql.connector.Error as err:
        conexao.rollback()
        print("Erro ao remover cliente:", err)
    finally:
        cursor.close()
        conexao.close()