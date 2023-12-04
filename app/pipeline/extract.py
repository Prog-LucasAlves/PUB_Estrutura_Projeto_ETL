"""Esse e o módulo de extração de dados."""
import glob  # Biblioteca para listar arquivos
import os  # Biblioteca para manipular arquivos e pastas
from typing import List  # Biblioteca para tipar os dados de retorno da função extract_from_excel()

import pandas as pd  # Biblioteca para manipular dados em dataframes e series


def extract_from_excel(path: str) -> List[pd.DataFrame]:
    """
    Função para ler os arquivos da pasta data/input e retornar uma lista de dataframes.

    args: input_path (str): caminho da pasta com os arquivos

    return: lista de dataframes
    """
    # Lista de arquivos do diretório input_path com extensão .xlsx
    all_files = glob.glob(os.path.join(path, '*.xlsx'))

    # Lista para armazenar os dataframes lidos do arquivo excel
    data_frame_list = []
    # Percorre a lista de arquivos do diretório input_path
    for file in all_files:
        # Lê o arquivo excel e retorna um dataframe
        data = pd.read_excel(file)
        # Adiciona o dataframe lido à lista de dataframes
        data_frame_list.append(data)

    # Retorna a lista de dataframes lidos do arquivo excel
    return data_frame_list


if __name__ == '__main__':
    data_frame_list = extract_from_excel('../data/input')
    print(data_frame_list)
