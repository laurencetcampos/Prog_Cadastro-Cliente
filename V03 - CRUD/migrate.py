import mysql.connector
import sqlite3
import os

print("Iniciando migracao...")
try:
    # Conectar ao MySQL
    mysql_conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='UNIVESP&Grupo',
        database='cadastro_clientes'
    )
    mysql_cursor = mysql_conn.cursor(dictionary=True)
    mysql_cursor.execute('SELECT * FROM clientes')
    clientes = mysql_cursor.fetchall()
    
    # Conectar/Criar SQLite
    sqlite_conn = sqlite3.connect('database.sqlite')
    sqlite_cursor = sqlite_conn.cursor()
    
    # Criar tabela clientes no SQLite
    sqlite_cursor.execute('''
    CREATE TABLE IF NOT EXISTS clientes(
        id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
        nome_cliente VARCHAR(30) NOT NULL,
        whatsapp VARCHAR(20) NOT NULL UNIQUE,
        endereco VARCHAR(50),
        cidade VARCHAR(30) NOT NULL,
        promocao_status BOOLEAN NOT NULL
    )
    ''')
    
    sqlite_cursor.execute('DELETE FROM clientes')
    
    for c in clientes:
        sqlite_cursor.execute('''
            INSERT INTO clientes (id_cliente, nome_cliente, whatsapp, endereco, cidade, promocao_status)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (c['id_cliente'], c['nome_cliente'], c['whatsapp'], c['endereco'], c['cidade'], c['promocao_status']))
    
    sqlite_conn.commit()
    sqlite_cursor.execute('SELECT COUNT(*) FROM clientes')
    total = sqlite_cursor.fetchone()[0]
    print(f'Total de registros importados pro SQLite: {total}')
    
    mysql_cursor.close()
    mysql_conn.close()
    sqlite_cursor.close()
    sqlite_conn.close()
except Exception as e:
    print(f"Erro na migracao: {e}")
