import pyodbc

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

# Criar tabela dim_cliente
cursor.execute('''
    IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='dim_cliente' AND xtype='U')
    CREATE TABLE dim_cliente (
        cliente_id INT PRIMARY KEY,
        nome_cliente VARCHAR(100),
        idade INT,
        genero VARCHAR(10),
        cidade VARCHAR(50),
        estado VARCHAR(50)
    )
''')

# Criar tabela dim_produto
cursor.execute('''
    IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='dim_produto' AND xtype='U')
    CREATE TABLE dim_produto (
        produto_id INT PRIMARY KEY,
        nome_produto VARCHAR(100),
        categoria VARCHAR(50),
        preco DECIMAL(10, 2)
    )
''')

# Criar tabela dim_tempo
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

# Criar tabela fato_vendas
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

# Commit das alterações
conn.commit()

# Fechar conexão
cursor.close()
conn.close()

print("Tabelas criadas com sucesso!")