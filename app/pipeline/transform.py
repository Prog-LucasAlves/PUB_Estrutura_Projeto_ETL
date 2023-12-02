"""Esse e o módulo para transformar os dados."""
from typing import List

import pandas as pd


def concat_data_frames(data_frames_list: List[pd.DataFrame]) -> pd.DataFrame:
    """
    Função para transformar uma lista de dataframes em um dataframe unificado.

    args: ...

    rertun: ...
    """
    return pd.concat(data_frames_list, ignore_index=True)
