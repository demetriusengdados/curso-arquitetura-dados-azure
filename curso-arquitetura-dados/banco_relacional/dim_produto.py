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

# Criar a tabela se não existir
cursor.execute('''
    IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='dim_produto' AND xtype='U')
    CREATE TABLE dim_produto (
        produto_id INT PRIMARY KEY,
        nome_produto VARCHAR(100),
        categoria VARCHAR(50),
        preco DECIMAL(10, 2)
    )
''')
conn.commit()

# Caminho do arquivo CSV
csv_file = os.path.join('output_files', 'dim_produto.csv')

# Ler e inserir os dados no banco
with open(csv_file, newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)  # Pular cabeçalho
    for row in reader:
        cursor.execute(
            "INSERT INTO dim_produto (produto_id, nome_produto, categoria, preco) VALUES (?, ?, ?, ?)",
            row[0], row[1], row[2], row[3]
        )

# Commit e fechar conexão
conn.commit()
cursor.close()
conn.close()

print("Carga concluída com sucesso!")

