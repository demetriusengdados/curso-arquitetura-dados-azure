CREATE TABLE fato_vendas (
    venda_id INT PRIMARY KEY,
    cliente_id INT,
    produto_id INT,
    tempo_id INT,
    quantidade INT,
    valor_total DECIMAL(10, 2),
    FOREIGN KEY (cliente_id) REFERENCES dim_cliente(cliente_id),
    FOREIGN KEY (produto_id) REFERENCES dim_produto(produto_id),
    FOREIGN KEY (tempo_id) REFERENCES dim_tempo(tempo_id)
);
