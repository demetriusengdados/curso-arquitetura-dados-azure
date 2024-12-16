CREATE TABLE dim_cliente( 
    cliente_id INT PRIMARY KEY,
    nome_cliente VARCHAR(100),
    idade INT,
    genero VARCHAR(10),
    cidade VARCHAR(50),
    estado VARCHAR(50)
);

--tabela dimensao produto

CREATE Table dim_produto(
    produto_id INT PRIMARY KEY,
    nome_produto VARCHAR(100),
    categoria VARCHAR(50),
    preco DECIMAL(10,2)
);

-- criando tabela dimensão tempo

CREATE Table dim_tempo(
    tempo_id INT PRIMARY KEY,
    data DATE,
    ano INT,
    mes INT,
    dia INT,
    trimestre INT
);

-- criando tabela fato vendas

CREATE Table fato_vendas(
    venda_id INT PRIMARY key,
    cliente_id INT,
    produto_id INT,
    tempo_id INT,
    quantidade INT,
    valor_total DECIMAL(10, 2),
    Foreign Key (cliente_id) REFERENCES dim_cliente(cliente_id),
    Foreign Key (produto_id) REFERENCES dim_produto(produto_id),
    Foreign Key (tempo_id) REFERENCES dim_tempo(tempo_id)
);
