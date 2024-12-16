import redis

# Conectando ao servidor Redis (assumindo que está rodando localmente na porta padrão 6379)
client = redis.Redis(host='localhost', port=6379, db=0)

# Adicionando 100 registros ao Redis
for i in range(100):
    key = f"key_{i}"
    value = f"value_{i}"
    client.set(key, value)

print("100 registros foram adicionados ao Redis com sucesso!")
