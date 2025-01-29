import pyodbc
import csv
import os

# Configuração da conexão com o SQL Server
server = 'localhost'  # Altere se necessário
port = '1433'
database = 'seu_banco_de_dados'  # Substitua pelo nome do seu banco de dados
username = 'sa'
password = 'SenhaForte123!'

conn_str = (
    f'DRIVER={{ODBC Driver 17 for SQL Server}};'
    f'SERVER={server},{port};'
    f'DATABASE={database};'
    f'UID={username};'
    f'PWD={password}'
)

# Criar conexão
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

# Criar a tabela dim_tempo se não existir
cursor.execute('''
    IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='dim_tempo' AND xtype='U')
    CREATE TABLE dim_tempo (
        tempo_id INT PRIMARY KEY,
        data DATE,
        ano INT,
        mes INT,
        dia INT,
        trimestre INT
    )
''')
conn.commit()

# Caminho dos arquivos CSV
csv_files = {
    'dim_tempo': os.path.join('output_files', 'dim_tempo.csv')
}

# Função para carregar CSV para SQL Server
def load_csv_to_sql(table_name, csv_file, insert_query):
    with open(csv_file, newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Pular cabeçalho
        for row in reader:
            cursor.execute(insert_query, row)
    conn.commit()

# Inserção de dados nas tabelas
load_csv_to_sql('dim_tempo', csv_files['dim_tempo'], 
    "INSERT INTO dim_tempo (tempo_id, data, ano, mes, dia, trimestre) VALUES (?, ?, ?, ?, ?, ?)")

# Fechar conexão
cursor.close()
conn.close()

print("Carga concluída com sucesso!")

