from faker import Faker
from pymongo import MongoClient
import pandas as pd
from sqlalchemy import create_engine
import pyodbc
import os

# Configuração para o Faker
fake = Faker()

# Configuração do MongoDB
mongo_client = MongoClient("mongodb://<username>:<password>@<your_mongo_host>:<your_mongo_port>")
db = mongo_client["my_database"]
collection = db["fake_data"]

# Configuração do SQL Server
SQL_SERVER_CONNECTION_STRING = "mssql+pyodbc://<username>:<password>@<server>/<database>?driver=ODBC+Driver+17+for+SQL+Server"

# Geração de dados fake
def generate_fake_data(num_records=100):
    data = []
    for _ in range(num_records):
        record = {
            "name": fake.name(),
            "email": fake.email(),
            "address": fake.address(),
            "phone_number": fake.phone_number(),
            "company": fake.company(),
            "job": fake.job(),
            "created_at": fake.date_time_this_year().isoformat(),
        }
        data.append(record)
    return data

# Inserção de dados no MongoDB
def load_data_to_mongo(data):
    collection.insert_many(data)
    print(f"{len(data)} records inserted into MongoDB.")

# Extração e transformação dos dados do MongoDB
def extract_and_transform():
    data = list(collection.find({}, {"_id": 0}))  # Ignorando o campo "_id"
    df = pd.DataFrame(data)
    
    # Exemplo de transformação: Adicionar uma nova coluna
    df["source"] = "MongoDB"
    return df

# Carregamento dos dados no SQL Server
def load_to_sqlserver(df):
    engine = create_engine(SQL_SERVER_CONNECTION_STRING)
    
    # Nome da tabela no SQL Server
    table_name = "fake_data"
    
    # Inserindo os dados transformados no SQL Server
    with engine.connect() as connection:
        df.to_sql(table_name, con=connection, if_exists="replace", index=False)
        print(f"Data loaded into SQL Server table: {table_name}")

# Pipeline de ETL completo
def etl_pipeline():
    # Etapa 1: Gerar dados fake
    print("Generating fake data...")
    fake_data = generate_fake_data(100)
    
    # Etapa 2: Inserir no MongoDB
    print("Loading data into MongoDB...")
    load_data_to_mongo(fake_data)
    
    # Etapa 3: Extrair e transformar os dados
    print("Extracting and transforming data...")
    transformed_data = extract_and_transform()
    
    # Etapa 4: Carregar no SQL Server
    print("Loading data into SQL Server...")
    load_to_sqlserver(transformed_data)
    
    print("ETL pipeline completed.")

if __name__ == "__main__":
    etl_pipeline()
