from sqlalchemy import create_engine
import pymysql

# Conexão com o banco MySQL
mysql_user = "usuario"
mysql_password = "senha"
mysql_host = "localhost"  # Host do MySQL
mysql_db = "nome_do_banco"

# Criando engine do MySQL
mysql_engine = create_engine(f"mysql+pymysql://{mysql_user}:{mysql_password}@{mysql_host}/{mysql_db}")

# Enviando os dados para uma tabela chamada "weather_data" no MySQL
df.to_sql("weather_data", mysql_engine, if_exists="replace", index=False)
print("Dados enviados para o MySQL.")
