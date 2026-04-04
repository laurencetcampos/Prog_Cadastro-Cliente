import sys
import os
import random

# Adiciona o diretório V02 - CRUD ao path para importar a conexão com o banco
sys.path.append(os.path.abspath('V02 - CRUD'))
from DB_connection import cnx

def generate_random_brazilian_phone():
    ddd = 15
    first_part = random.randint(90000, 99999)
    second_part = random.randint(1000, 9999)
    return f"({ddd}) {str(first_part)[:5]}-{str(second_part).zfill(4)}"

nomes_primeiro = ["Ana", "Joao", "Maria", "Pedro", "Lucas", "Mariana", "Julia", "Carlos", "Marcos", "Fernanda", "Roberto", "Rafael", "Camila", "Rodrigo", "Leticia", "Guilherme", "Aline", "Felipe", "Thiago", "Beatriz", "Ricardo", "Amanda", "Marcelo", "Bruno", "Patricia", "Juliana", "Eduardo"]
sobrenomes = ["Silva", "Santos", "Oliveira", "Souza", "Rodrigues", "Ferreira", "Alves", "Pereira", "Lima", "Gomes", "Costa", "Ribeiro", "Martins", "Carvalho", "Almeida", "Lopes", "Soares", "Fernandes", "Vieira", "Mendes", "Dias", "Cardoso", "Rocha", "Neves", "Teixeira"]

cidades = ["Sorocaba"] * 10 + ["Votorantim", "Itu", "Piedade", "Salto de Pirapora", "Aracoiaba da Serra", "Ipero", "Boituva"]
ruas = ["Rua das Flores", "Av Brasil", "Rua Sao Joao", "Rua XV de Novembro", "Av Ipanema", "Av Itavuvu", "Rua Aparecida", "Rua da Penha", "Av Afonso Vergueiro", "Rua Sete de Setembro", "Rua da Esperanca", "Av Sao Paulo", "Rua Central"]

try:
    conexao = cnx()
    if conexao is None:
        print("Falha ao conectar ao banco MySQL.")
        sys.exit(1)
        
    cursor = conexao.cursor()
    
    sucesso_count = 0
    for _ in range(30):
        # Gera nome (dois sobrenomes)
        nome = f"{random.choice(nomes_primeiro)} {random.choice(sobrenomes)} {random.choice(sobrenomes)}"
        # Para evitar repetição de sobrenome
        while len(set(nome.split()[1:])) == 1:
            nome = f"{random.choice(nomes_primeiro)} {random.choice(sobrenomes)} {random.choice(sobrenomes)}"
            
        whatsapp = generate_random_brazilian_phone()
        endereco = f"{random.choice(ruas)}, {random.randint(10, 2000)}"
        cidade = random.choice(cidades)
        promocao_status = random.choice([True, False])
        
        query = "INSERT INTO clientes (nome_cliente, whatsapp, endereco, cidade, promocao_status) VALUES (%s, %s, %s, %s, %s)"
        val = (nome[:30], whatsapp[:20], endereco[:50], cidade[:30], promocao_status)
        
        try:
            cursor.execute(query, val)
            sucesso_count += 1
        except Exception as e:
            # Continua mesmo se der erro (ex: numero unico repetido, raro mas possivel)
            print(f"Erro ao inserir {nome}: {e}")
            
    conexao.commit()
    print(f"Inseridos {sucesso_count} registros com sucesso.")
    cursor.close()
    conexao.close()
except Exception as e:
    print(f"Erro geral: {e}")
