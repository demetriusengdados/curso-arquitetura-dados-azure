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
