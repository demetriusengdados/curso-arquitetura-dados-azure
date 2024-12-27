import requests
import pandas as pd

# Substitua pela sua chave de API do OpenWeatherMap
API_KEY = "05fb3e5a1b37d1048811a512fd8cc1b6"
CITY = "São Paulo"  # Nome da cidade desejada
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# Fazendo a requisição para a API
params = {
    "q": CITY,
    "appid": API_KEY,
    "units": "metric"  # Unidade métrica (Celsius)
}
response = requests.get(BASE_URL, params=params)
data = response.json()

# Extraindo os dados principais e convertendo para DataFrame
weather_data = {
    "City": [data["name"]],
    "Temperature (°C)": [data["main"]["temp"]],
    "Humidity (%)": [data["main"]["humidity"]],
    "Pressure (hPa)": [data["main"]["pressure"]],
    "Weather": [data["weather"][0]["description"]]
}
df = pd.DataFrame(weather_data)
print(df)

# Criando uma pasta para salvar os arquivos
import os

output_folder = "output_files"
os.makedirs(output_folder, exist_ok=True)

# Salvando em CSV
csv_path = os.path.join(output_folder, "weather_data.csv")
df.to_csv(csv_path, index=False)

# Salvando em Excel
excel_path = os.path.join(output_folder, "weather_data.xlsx")
df.to_excel(excel_path, index=False)

# Salvando em Parquet
parquet_path = os.path.join(output_folder, "weather_data.parquet")
df.to_parquet(parquet_path, index=False)

print(f"Arquivos salvos em:\nCSV: {csv_path}\nExcel: {excel_path}\nParquet: {parquet_path}")