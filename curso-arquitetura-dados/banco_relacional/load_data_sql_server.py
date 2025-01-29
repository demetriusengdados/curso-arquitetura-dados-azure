import pyodbc
import csv

# Configurações do banco de dados
db_config = {
    "driver": "{ODBC Driver 17 for SQL Server}",  # Certifique-se de ter o driver instalado
    "server": "localhost",                       # Nome ou IP do servidor
    "database": "seu_banco",                     # Nome do banco de dados
    "username": "demetrius",                     # Usuário do SQL Server
    "password": "123456789"                      # Senha do SQL Server
}

# Caminho do arquivo CSV gerado
csv_file_path = "dim_cliente.csv"

try:
    # Conectando ao SQL Server
    conn = pyodbc.connect(
        f"DRIVER={db_config['driver']};"
        f"SERVER={db_config['server']};"
        f"DATABASE={db_config['database']};"
        f"UID={db_config['username']};"
        f"PWD={db_config['password']}"
    )
    cursor = conn.cursor()
    print("Conexão com o SQL Server estabelecida.")

    # Leitura do arquivo CSV
    with open(csv_file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Pula o cabeçalho

        # Inserção linha por linha
        for row in reader:
            cursor.execute("""
                INSERT INTO dim_cliente (cliente_id, nome_cliente, idade, genero, cidade, estado)
                VALUES (?, ?, ?, ?, ?, ?)
            """, row)
    
    # Commit para salvar as mudanças
    conn.commit()
    print("Dados inseridos com sucesso no SQL Server!")

except Exception as e:
    print(f"Erro ao inserir os dados: {e}")
    if conn:
        conn.rollback()  # Reverte alterações em caso de erro
finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()
        print("Conexão com o SQL Server encerrada.")
