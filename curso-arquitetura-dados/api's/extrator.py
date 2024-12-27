import requests
import json

def extract_data_from_api(api_url, headers=None, params=None):
    """
    Extrai dados de uma API.
    
    Args:
        api_url (str): URL da API.
        headers (dict): Cabeçalhos da requisição (opcional).
        params (dict): Parâmetros da query string (opcional).
        
    Returns:
        dict: Dados retornados pela API.
    """
    try:
        # Fazendo a requisição GET
        response = requests.get(api_url, headers=headers, params=params)

        # Verificando se o status da requisição foi bem-sucedido (200)
        response.raise_for_status()

        # Convertendo a resposta para JSON
        data = response.json()
        return data

    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a API: {e}")
        return None

# Exemplo de uso:
if __name__ == "__main__":
    # URL da API
    api_url = "https://api.exemplo.com/data"

    # Headers (se necessário)
    headers = {
        "Authorization": "Bearer seu_token_aqui",  # Caso a API use autenticação
        "Content-Type": "application/json"
    }

    # Parâmetros (se necessário)
    params = {
        "param1": "valor1",
        "param2": "valor2"
    }

    # Extraindo os dados
    data = extract_data_from_api(api_url, headers, params)

    # Exibindo os dados extraídos
    if data:
        print(json.dumps(data, indent=4, ensure_ascii=False))
