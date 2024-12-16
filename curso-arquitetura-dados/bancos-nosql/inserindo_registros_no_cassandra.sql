--Criando as tabelas 
CREATE TABLE users (
    id UUID PRIMARY KEY,
    name TEXT,
    email TEXT,
    age INT
);

--Inserindo usuarios a tabela
INSERT INTO users (id, name, email, age) 
VALUES (uuid(), 'John Doe', 'john.doe@example.com', 30);


INSERT INTO users (id, name, email, age) 
VALUES (uuid(), 'Alice Smith', 'alice.smith@example.com', 25);

INSERT INTO users (id, name, email, age) 
VALUES (uuid(), 'Bob Johnson', 'bob.johnson@example.com', 40);

--Usar Prepared Statements é uma prática recomendada para otimizar a performance e a segurança.
PREPARED insert_user FROM 
'INSERT INTO users (id, name, email, age) VALUES (?, ?, ?, ?)';

--Executar a instrução preparada com os valores desejados:
EXECUTE insert_user (uuid(), 'Eve Adams', 'eve.adams@example.com', 35);



