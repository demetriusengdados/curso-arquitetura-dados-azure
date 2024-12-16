CREATE KEYSPACE ecommerce
WITH replication = {
  'class': 'SimpleStrategy',
  'replication_factor': 3
};


CREATE KEYSPACE staging
WITH replication = {
  'class': 'raw',
  'replication_factor': 3
};

CREATE KEYSPACE homologacao
WITH replication = {
  'class': 'silver',
  'replication_factor' : 3  
};

CREATE KEYSPACE producao
WITH replication = {
  'class' : 'gold',
  'replicatio_factor' : 3
};