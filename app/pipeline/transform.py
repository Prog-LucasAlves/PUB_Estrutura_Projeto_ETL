"""Esse e o módulo para transformar os dados."""
from typing import List  # Biblioteca para tipar os dados de retorno da função concat_data_frames()

import pandas as pd  # Biblioteca para trabalhar com dataframes e series


def concat_data_frames(data_frames_list: List[pd.DataFrame]) -> pd.DataFrame:
    """
    Função para transformar uma lista de dataframes em um dataframe unificado.

    args: ...

    rertun: ...
    """
    # Concatena os dataframes da lista em um dataframe unificado.
    # Ignora os índices dos dataframes concatenados.
    # Retorna o dataframe concatenado.
    return pd.concat(data_frames_list, ignore_index=True)
