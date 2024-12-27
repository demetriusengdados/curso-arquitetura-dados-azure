from sqlalchemy import create_engine
import psycopg2

# Conexão com o banco PostgreSQL
postgres_user = "usuario"
postgres_password = "senha"
postgres_host = "localhost"  # Host do PostgreSQL
postgres_db = "nome_do_banco"

# Criando engine do PostgreSQL
postgres_engine = create_engine(f"postgresql+psycopg2://{postgres_user}:{postgres_password}@{postgres_host}/{postgres_db}")

# Enviando os dados para uma tabela chamada "weather_data" no PostgreSQL
df.to_sql("weather_data", postgres_engine, if_exists="replace", index=False)
print("Dados enviados para o PostgreSQL.")
