from pymongo import MongoClient

# URL de conexão ao MongoDB (substitua pela sua)
# Para um servidor local
uri = "mongodb://localhost:27017"

# Para MongoDB Atlas
# uri = "mongodb+srv://<user>:<password>@cluster0.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

# Nome do banco de dados
db_name = "meuBanco"

def connect_to_database():
    # Criando um cliente do MongoDB
    client = MongoClient(uri)

    try:
        # Conectando ao banco de dados
        print("Conectando ao MongoDB...")
        db = client[db_name]
        print(f"Conexão bem-sucedida ao banco de dados: {db_name}")

        # Exemplo: Listar as coleções no banco de dados
        collections = db.list_collection_names()
        print(f"Coleções no banco de dados: {collections}")

        return db
    except Exception as e:
        print("Erro ao conectar ao MongoDB:", e)
    finally:
        # Fechando a conexão
        client.close()
        print("Conexão fechada.")

# Executar a função
if __name__ == "__main__":
    connect_to_database()
