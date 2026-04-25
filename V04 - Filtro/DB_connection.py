import sqlite3
import os
import sys
import shutil

def get_db_path():
    # Quando rodado pelo PyInstaller, usa o diretório onde o executável final está
    if getattr(sys, 'frozen', False):
        application_path = os.path.dirname(sys.executable)
        temp_path = sys._MEIPASS
    else:
        application_path = os.path.dirname(os.path.abspath(__file__))
        temp_path = application_path
        
    db_path = os.path.join(application_path, 'database.sqlite')
    
    # Se o aplicativo for recém-aberto e não houver base, copia a base salva internamente
    if not os.path.exists(db_path):
        embedded_db = os.path.join(temp_path, 'database.sqlite')
        if os.path.exists(embedded_db) and embedded_db != db_path:
            shutil.copy2(embedded_db, db_path)
            
    return db_path

def cnx():
    try:
        # SQLite embutido
        conexao = sqlite3.connect(get_db_path())
        # Habilita suporte a chaves estrangeiras, se necessário
        conexao.execute("PRAGMA foreign_keys = 1")
        # Prepara a conexão para retornar dicionários ao invés de tuplas
        conexao.row_factory = sqlite3.Row
        return conexao
    except Exception as err:
        print("Erro ao conectar com SQLite:", err)
        return None