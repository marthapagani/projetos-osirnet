# Instale a biblioteca pygsheets se ainda não estiver instalada
# pip install pygsheets

import pygsheets

# Autentique-se com suas credenciais do Google Sheets
gc = pygsheets.authorize(service_file='projetos-osirnet\Python\dif-horas\config.json')

# Abra a planilha pelo nome
spreadsheet = gc.open('RNP Cálculos')

# Selecione uma guia específica (opcional)
worksheet = spreadsheet.sheet1

# Exemplo: Insira dados na célula A1
worksheet.update_value('F1', 'Hello, Google Sheets!')

# Exemplo: Leitura de dados da célula A1
data = worksheet.get_value('F1')
print(f'Data in F1: {data}')
