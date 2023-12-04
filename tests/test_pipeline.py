import pandas as pd

from app.pipeline.transform import concat_data_frames

# cria dois dataframes com 2 linhas e 2 colunas cada
df_1 = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
df_2 = pd.DataFrame({'col1': [5, 6], 'col2': [7, 8]})


def testar_a_concatenacao_da_lista_de_dataframe():
    """"""
    # arrange
    data_frame_list = [df_1, df_2]  # lista de dataframes

    # act
    df = concat_data_frames(data_frame_list)  # dataframe concatenado

    # assert
    # verifica se o dataframe tem 4 linhas e 2 colunas
    assert df.shape == (4, 2)
    # verifica se o primeiro valor da primeira linha é 1
    assert df.iloc[0, 0] == 1
    # verifica se o segundo valor da primeira linha é 3
    assert df.iloc[0, 1] == 3
