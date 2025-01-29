import os
import pyodbc

# Configurações do banco de dados
server = 'SEU_SERVIDOR'
database = 'SEU_BANCO'
username = 'SEU_USUARIO'
password = 'SUA_SENHA'
driver = '{ODBC Driver 17 for SQL Server}'

# Conectar ao banco de dados
conn = pyodbc.connect(
    f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'
)
cursor = conn.cursor()

# Criar a tabela dim_cliente
cursor.execute('''
CREATE TABLE IF NOT EXISTS dim_cliente (
    cliente_id INT PRIMARY KEY,
    nome_cliente VARCHAR(100),
    idade INT,
    genero VARCHAR(10),
    cidade VARCHAR(50),
    estado VARCHAR(50)
);
''')
conn.commit()

# Caminho do arquivo CSV
csv_file = os.path.join("output_files", "dim_cliente.csv")

# Carregar dados do CSV para o DataFrame
if os.path.exists(csv_file):
    df = pd.read_csv(csv_file)
    
    # Inserir dados na tabela
    for index, row in df.iterrows():
        cursor.execute('''
        INSERT INTO dim_cliente (cliente_id, nome_cliente, idade, genero, cidade, estado)
        VALUES (?, ?, ?, ?, ?, ?)
        ''', row['cliente_id'], row['nome_cliente'], row['idade'], row['genero'], row['cidade'], row['estado'])
    
    conn.commit()
    print("Dados inseridos com sucesso!")
else:
    print("Arquivo CSV não encontrado!")

# Fechar conexão
cursor.close()
conn.close()

