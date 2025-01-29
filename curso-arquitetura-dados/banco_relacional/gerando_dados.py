import os
import csv
import random
from faker import Faker

def generate_fake_data():
    fake = Faker()
    
    # Diretório de saída
    output_dir = "output_files"
    os.makedirs(output_dir, exist_ok=True)
    
    # Quantidade de registros
    num_produtos = 500
    num_clientes = 1000
    num_tempos = 365
    num_vendas = 10000

    # Geração de dados para a tabela dim_produto
    produtos = []
    for produto_id in range(1, num_produtos + 1):
        nome_produto = fake.word().capitalize()
        categoria = random.choice(['Eletrônicos', 'Roupas', 'Livros', 'Móveis', 'Alimentos'])
        preco = round(random.uniform(10, 5000), 2)
        produtos.append([produto_id, nome_produto, categoria, preco])

    # Geração de dados para a tabela dim_cliente
    clientes = []
    for cliente_id in range(1, num_clientes + 1):
        nome_cliente = fake.name()
        idade = random.randint(18, 80)
        genero = random.choice(['Masculino', 'Feminino'])
        cidade = fake.city()
        estado = fake.state()
        clientes.append([cliente_id, nome_cliente, idade, genero, cidade, estado])

    # Geração de dados para a tabela dim_tempo
    tempos = []
    for tempo_id in range(1, num_tempos + 1):
        data = fake.date_between(start_date="-1y", end_date="today")
        ano = data.year
        mes = data.month
        dia = data.day
        trimestre = (mes - 1) // 3 + 1
        tempos.append([tempo_id, data, ano, mes, dia, trimestre])

    # Geração de dados para a tabela fato_vendas
    vendas = []
    for venda_id in range(1, num_vendas + 1):
        cliente_id = random.randint(1, num_clientes)
        produto_id = random.randint(1, num_produtos)
        tempo_id = random.randint(1, num_tempos)
        quantidade = random.randint(1, 10)
        valor_total = round(quantidade * produtos[produto_id - 1][3], 2)  # preço x quantidade
        vendas.append([venda_id, cliente_id, produto_id, tempo_id, quantidade, valor_total])

    # Função para salvar arquivos CSV
    def save_to_csv(filename, headers, data):
        filepath = os.path.join(output_dir, filename)
        with open(filepath, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(headers)
            writer.writerows(data)

    save_to_csv("dim_produto.csv", ["produto_id", "nome_produto", "categoria", "preco"], produtos)
    save_to_csv("dim_cliente.csv", ["cliente_id", "nome_cliente", "idade", "genero", "cidade", "estado"], clientes)
    save_to_csv("dim_tempo.csv", ["tempo_id", "data", "ano", "mes", "dia", "trimestre"], tempos)
    save_to_csv("fato_vendas.csv", ["venda_id", "cliente_id", "produto_id", "tempo_id", "quantidade", "valor_total"], vendas)

    print("Arquivos CSV gerados com sucesso na pasta output_files!")

# Executar geração de dados
generate_fake_data()