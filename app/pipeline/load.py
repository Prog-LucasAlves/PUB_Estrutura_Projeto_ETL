"""Esse e o módulo para carregar os dados."""
import os  # Biblioteca para manipular caminhos de arquivos e diretórios

import pandas as pd  # Biblioteca para trabalhar com dataframes e series


def load_excel(
    data_frame: pd.DataFrame, output_path: str, file_name: str
) -> str:
    """
    Receber um dataframe e salvar como excel.

    args:
    data_frame (pd.DataFrame): dataframe a ser salvo como excel
    output_path (str): caminho para salvar o arquivo
    file_name (str): nome do arquivo a ser salvo

    return: "Arquivo salvo com sucesso"

    """
    # Verifica se o diretório de saída existe, se não existir, cria o diretório.
    if not os.path.exists(output_path):
        # Cria o diretório de saída
        os.makedirs(output_path)

    # Salva o dataframe como um arquivo excel no diretório de saída.
    data_frame.to_excel(f'{output_path}/{file_name}.xlsx', index=False)
    # Retorna uma mensagem de sucesso.
    return 'Arquivo salvo com sucesso'
