CREATE TABLE product_sales (
  product_id UUID,             -- ID do produto
  sales_date DATE,             -- Data da venda
  total_sales DECIMAL,         -- Total de vendas do dia
  quantity_sold INT,           -- Quantidade de produtos vendidos
  PRIMARY KEY (product_id, sales_date)
);
