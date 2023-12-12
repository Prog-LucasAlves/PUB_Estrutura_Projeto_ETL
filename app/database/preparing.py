"""Esse modulo prepara o arquivo Excel para ser inserido no banco de dados"""
import conectdb  # Importa o modulo de conexao com o banco de dados
import openpyxl  # Importa o modulo de leitura de arquivos Excel

# Salva o local do arquivo Excel em uma variavel
excel_file = "../../data/output/output.xlsx"
# Carrega o arquivo Excel em um objeto Workbook
wb = openpyxl.load_workbook(excel_file)
# Seleciona a primeira aba do arquivo Excel
sheet = wb.active
# Cria uma lista com os nomes das colunas do arquivo Excel
column_names = [column.value for column in sheet[1]]
# Cria uma lista vazia para armazenar os dados do arquivo Excel
data = []
# Itera sobre as linhas do arquivo Excel, ignorando a primeira linha (com os nomes das colunas)
for row in sheet.iter_rows(min_row=2, values_only=True):
    data.append(row)

# Nome para o Schema e tabela no banco de dados
schema_name = "hr_colaboradores"
table_name = "evaluation"

# Query para criar o schema do banco de dados
schema_creation_query = f"CREATE SCHEMA IF NOT EXISTS {schema_name}"

# Query para criar a tabela do banco de dados com os nomes das colunas
table_creation_query = f"""
CREATE TABLE IF NOT EXISTS {schema_name}.{table_name} (
 {", ".join([f'"{name}" TEXT' for name in column_names])})
 """

# Query para criar a tabela no banco de dados
conectdb.cursor(schema_creation_query)
conectdb.cursor(table_creation_query)

# Query para inserir os dados do arquivo Excel na tabela do banco de dados
insert_data_query = f"""
   INSERT INTO {schema_name}.{table_name} ({", ".join([f'"{name}"' for name in column_names])})
   VALUES ({", ".join(['%s' for _ in column_names])})
"""

# Executa a query para inserir os dados do arquivo Excel na tabela do banco de dados
conectdb.cursormany(insert_data_query, data)
