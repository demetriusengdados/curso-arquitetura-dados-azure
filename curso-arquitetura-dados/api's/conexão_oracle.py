from sqlalchemy import create_engine
import cx_Oracle

# Conexão com o banco Oracle
oracle_user = "usuario"
oracle_password = "senha"
oracle_dsn = "host:porta/servico"  # Exemplo: "localhost:1521/xe"

# Criando engine do Oracle
oracle_engine = create_engine(f"oracle+cx_oracle://{oracle_user}:{oracle_password}@{oracle_dsn}")

# Enviando os dados para uma tabela chamada "weather_data" no Oracle
df.to_sql("weather_data", oracle_engine, if_exists="replace", index=False)
print("Dados enviados para o Oracle.")
