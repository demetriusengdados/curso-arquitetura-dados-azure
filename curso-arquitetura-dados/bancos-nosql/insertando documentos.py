import pymongo

# Conexão ao MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["curso-pós"]
collection = db["mycollection"]

# Geração de dados de exemplo
data = []
for i in range(1000):
    data.append({
        "nome": f"Nome {i}",
        "idade": i % 100,
        "cidade": f"Cidade {i % 10}",
        "email": f"email{i}@example.com"
    })

# Inserção dos dados na coleção
collection.insert_many(data)

# Impressão de mensagem de sucesso
print("Dados inseridos com sucesso!")
