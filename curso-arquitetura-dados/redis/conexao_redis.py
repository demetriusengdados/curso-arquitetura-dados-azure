import redis

# Configurando a conexão com o Redis
redis_client = redis.Redis(
    host='localhost',  # Endereço do servidor Redis
    port=6379,         # Porta padrão do Redis
    db=0               # Número do banco de dados (0 é o padrão)
)

# Testando a conexão
try:
    # Tentando um comando básico no Redis para verificar a conexão
    response = redis_client.ping()
    if response:
        print("Conexão com Redis estabelecida com sucesso!")
except redis.ConnectionError as e:
    print(f"Erro ao conectar com o Redis: {e}")
