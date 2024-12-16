CREATE INDEX ON orders (status); -- Índice no campo status


CREATE TABLE session_data (
  session_id UUID PRIMARY KEY, -- ID da sessão
  user_id UUID,                -- ID do usuário
  login_time TIMESTAMP         -- Hora do login
) WITH default_time_to_live = 3600; -- Dados expiram em 1 hora


INSERT INTO orders (order_id, user_id, product_id, order_date, status, total_amount)
VALUES (uuid(), uuid(), uuid(), toTimestamp(now()), 'Pendente', 199.99);


UPDATE orders
SET status = 'Enviado'
WHERE order_id = {ORDER_ID};
