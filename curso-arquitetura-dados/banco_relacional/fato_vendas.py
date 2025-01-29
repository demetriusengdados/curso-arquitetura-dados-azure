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

# Criar a tabela fato_vendas se não existir
cursor.execute('''
    IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='fato_vendas' AND xtype='U')
    CREATE TABLE fato_vendas (
        venda_id INT PRIMARY KEY,
        cliente_id INT,
        produto_id INT,
        tempo_id INT,
        quantidade INT,
        valor_total DECIMAL(10, 2),
        FOREIGN KEY (cliente_id) REFERENCES dim_cliente(cliente_id),
        FOREIGN KEY (produto_id) REFERENCES dim_produto(produto_id),
        FOREIGN KEY (tempo_id) REFERENCES dim_tempo(tempo_id)
    )
''')
conn.commit()

# Caminho do arquivo CSV para fato_vendas
csv_file_fato_vendas = os.path.join('output_files', 'fato_vendas.csv')

# Função para carregar CSV para SQL Server
def load_csv_to_sql(table_name, csv_file, insert_query):
    with open(csv_file, newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Pular cabeçalho
        for row in reader:
            cursor.execute(insert_query, row)
    conn.commit()

# Inserção de dados na tabela fato_vendas
load_csv_to_sql('fato_vendas', csv_file_fato_vendas, 
    "INSERT INTO fato_vendas (venda_id, cliente_id, produto_id, tempo_id, quantidade, valor_total) VALUES (?, ?, ?, ?, ?, ?)")

# Fechar conexão
cursor.close()
conn.close()

print("Carga da tabela fato_vendas concluída com sucesso!")