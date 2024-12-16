from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

# Informações de autenticação, se necessário
auth_provider = PlainTextAuthProvider(username='demetrius.mata', password='Dados2024#')

# Conectando ao cluster
cluster = Cluster(['127.0.0.1'], auth_provider=auth_provider)
session = cluster.connect()

# Selecionando um keyspace (se aplicável)
session.set_keyspace('ecommerce')

# Teste de conexão executando uma query
result = session.execute("SELECT release_version FROM system.local")
for row in result:
    print("Versão do Cassandra:", row.release_version)

# Fechando a conexão
cluster.shutdown()
