CREATE TABLE user_orders (
  user_id UUID,             -- ID do usuário
  order_date TIMESTAMP,     -- Data do pedido
  order_id UUID,            -- ID do pedido
  product_id UUID,          -- Produto comprado
  total_amount DECIMAL,     -- Valor total do pedido
  PRIMARY KEY (user_id, order_date)
) WITH CLUSTERING ORDER BY (order_date DESC);
