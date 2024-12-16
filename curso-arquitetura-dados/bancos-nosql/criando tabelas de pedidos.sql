USE ecommerce;

CREATE TABLE orders (
  order_id UUID PRIMARY KEY, -- Chave primária única
  user_id UUID,              -- ID do usuário que fez o pedido
  product_id UUID,           -- ID do produto comprado
  order_date TIMESTAMP,      -- Data do pedido
  status TEXT,               -- Status do pedido (Ex: "Pendente", "Enviado")
  total_amount DECIMAL       -- Valor total do pedido
);
