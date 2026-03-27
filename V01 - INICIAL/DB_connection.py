# Importa a biblioteca para conectar ao MySQL
import mysql.connector

# Configurações de conexão com o banco de dados MySQL
# ATENÇÃO: Preencha com suas credenciais reais (user, password, host, database)
config = {
    'user': '',  # Nome do usuário do MySQL
    'password': '',  # Senha do usuário
    'host': '',  # Endereço do servidor MySQL (ex: 'localhost')
    'database': ''  # Nome do banco de dados
}

# Função para estabelecer conexão com o banco de dados
def cnx():
    try:
        # Tenta conectar usando as configurações
        conexao = mysql.connector.connect(**config)
        print("Conectado com sucesso!")
        return conexao  # Retorna a conexão se bem-sucedida
    except mysql.connector.Error as err:
        # Em caso de erro, imprime a mensagem e retorna None
        print("Erro ao conectar com MySQL:", err)
        return None