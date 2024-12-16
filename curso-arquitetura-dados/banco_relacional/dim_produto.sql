CREATE TABLE dim_produto (
    produto_id INT PRIMARY KEY,
    nome_produto VARCHAR(100),
    categoria VARCHAR(50),
    preco DECIMAL(10, 2)
);
